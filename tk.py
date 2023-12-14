import cv2
cam = cv2.VideoCapture(0)

k=0
a=0

def capture_frame(cam,k ):
    img_counter = 0
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Python Webcam Screenshot App")
    ret,frame = cam.read()
    if not ret:
        print("Failed to grab frame")
    cv2.imshow("test",frame)
    if k%256 == 27:
        print("Escape hit, closing the app")
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        
        cv2.imwrite(img_name,frame)
        print("Screenshot Taken")
        
    # cam.release()
    # cam.destroyAllWindows()

from tkinter import *

var = Tk()



def leftclick(event): 
    k=32
    capture_frame(cam,k )
    

def rightclick(event):
    k=27
    capture_frame(cam,k)
    
frame = Frame(var, width=300, height=250)
 
frame.bind("<Button-1>", leftclick)
 
frame.bind("<Button-3>", rightclick)
 
frame.pack()
 
var.mainloop()

