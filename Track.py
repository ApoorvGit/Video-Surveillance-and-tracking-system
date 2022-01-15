import sqlite3 as sl
import tkinter  as tk 
from tkinter import * 
from PIL import Image, ImageTk
# from datetime import datetime


con = sl.connect('data.db')
my_w = tk.Tk()
my_w.geometry("500x300") 

# Roll No
roll_text = StringVar()
roll_label = Label(my_w, text='Roll NO', font=('bold', 14))
roll_label.grid(row=0, column=2, sticky=W)
roll_entry = Entry(my_w, textvariable=roll_text)
roll_entry.grid(row=0, column=3)

b1 = tk.Button(my_w, text='Show Details', width=15,bg='green',
    command=lambda: my_details() )
b1.grid(row=1,column=3) 


#Result

name_str = tk.StringVar()
Name = tk.Label(my_w,  textvariable=name_str, width=30)  
Name.grid(row=3, column=2) 
name_str.set(" ")

loc_str = tk.StringVar()
loc = tk.Label(my_w,  textvariable=loc_str, width=30)  
loc.grid(row=5, column=2) 
loc_str.set(" ")

time_str = tk.StringVar()
Time = tk.Label(my_w,  textvariable=time_str, width=30 )  
Time.grid(row=6, column=2) 
time_str.set(" ")

def my_details():
    roll=str(roll_text.get())
    with con:
        query="SELECT name, location, time FROM USER where id=(?)"
        inp=(roll,)
        data = con.execute(query,inp)
        for row in data:
            name_str.set('Name: '+row[0])
            img=Image.open('images/'+str(roll)+'.jpg')
            img=img.resize((100,100)) # new width & height
            img=ImageTk.PhotoImage(img)
            e1 =Label(my_w,image=img)
            e1.grid(row=4,column=2)
            e1.image = img
            e1['image']=img # garbage collection 
            loc_str.set('Last Known Location: '+row[1])
            timestamp=row[2]
            # dt_object = datetime.fromtimestamp(timestamp)
            time_str.set('Time: '+str(timestamp))
            #print(str(name)+" "+str(location)+" "+str(time))
my_details()
my_w.mainloop()