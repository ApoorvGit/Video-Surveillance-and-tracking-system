import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import shutil
import sqlite3 as sl
from main import *

con = sl.connect('data.db')
  

my_w = tk.Tk()
my_w.geometry("560x300")  # Size of the window 
my_w.title('Face Entry System')

# Name
name_text = StringVar()
name_label = Label(my_w, text='Name', font=('bold', 14), pady=20)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(my_w, textvariable=name_text)
name_entry.grid(row=0, column=1 )

# Roll No
roll_text = StringVar()
roll_label = Label(my_w, text='Roll NO', font=('bold', 14))
roll_label.grid(row=0, column=2, sticky=W)
roll_entry = Entry(my_w, textvariable=roll_text)
roll_entry.grid(row=0, column=3)

#image
img_label = tk.Label(my_w,text='Select Image',font=('bold', 14), pady=20)  
img_label.grid(row=1,column=0,sticky=W)
b1 = tk.Button(my_w, text='Upload Files',command = lambda:upload_file())
b1.grid(row=1,column=1)

#output
out = Label(my_w, text='Added to DB', font=('bold', 14))


#start camera operation
cam_b = tk.Button(my_w, text='Start Cam', command = lambda:cctv())
cam_b.grid(row=9,column=1)

def clear_text(im, but):
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    out.configure(text="")
    im.config(image='')
    but.destroy()

def upload_file():
    f_types = [('Jpg Files', '*.jpg')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        roll=roll_text.get()
        sql = 'INSERT INTO USER (id, name, location) values(?, ?, ?)'
        data = (roll, name_text.get(), 'Main Gate')
        with con:
            con.execute(sql, data)
        shutil.copy(img.filename, 'images/'+roll+'.jpg')

        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =Label(my_w,image=img)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img # garbage collection 
        
        out.grid(row=7, column=1)
        b2 = tk.Button(my_w, text='Add New',command = lambda:clear_text(e1,b2))
        b2.grid(row=8,column=1)
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column                 
my_w.mainloop()  # Keep the window open