import cv2
from simple_facerec import SimpleFacerec
import sqlite3 as sl
import time 

def cctv():

    con = sl.connect('data.db')

    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(2)


    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, ids = sfr.detect_known_faces(frame)
        for face_loc, id in zip(face_locations, ids):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            name=""
            if id=="Unknown":
                color=(0,0,200)
                name="Unknown"
            else:
                color=(0,200,0)
                query="UPDATE USER SET location=?, time= ?  where id="+id
                data=('Hostel O', time.time())
                with con:
                    con.execute(query, data)
                with con:
                    data = con.execute("SELECT name FROM USER WHERE id= "+ id)
                    for row in data:
                        name=row[0]
                print(name)
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
#cctv()



