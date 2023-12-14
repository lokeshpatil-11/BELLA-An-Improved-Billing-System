import cv2
import veryfi
import pprint
import os
import glob
from tkinter import *

#setting the directory for a specific folder
os.chdir(r"C:\Users\LENOVO\Bella")

#function to empty the contents of the folder being used
def trunc():
    dir = r"C:\Users\LENOVO\Bella"
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

trunc()

#function to capture images 
#and store in orderly fashion in a folder
def cam_captr():        
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Python Webcam Screenshot App")

    img_counter = 0
    
    #while loop is used to cick all products in a bill a time
    while True:
        ret,frame = cam.read()

        if not ret:
            print("Failed to grab frame")
            return False
            break
        
        cv2.imshow("test",frame)
        k = cv2.waitKey(1)

        if k%256 == 27:
            print("Escape hit, closing the app")
            break

        elif k%256 == 32:
            # the name is specified in a pattern to ensure that,
            # before every new bill the previous data is discarded
            img_name = "product_{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            print("Screenshot Taken")
            img_counter +=1   

    cam.release()
    cam.destroyAllWindows()

    return True


try:
    cam_captr()   
except:
    print()

# used to put all the products in as single list
prod_list=list(os.listdir())
print(prod_list)

# setting the identity of the user as a ***shop_keeper***
# all of them can be obtained by registring with us
shop_keeper_id = "vrftXjKwnRGHG5RVtV7KhSOpwWNUp03LdZhtRGm"
shop_keeper_secret = "P2nImuUmbJsdpRCSJFtOSsBFlxXWEm6hIrGCtlPaeeZ8xVXsVu2iZHxnbVtPWUZj1LjOGCznzXlpvz6jjLBEsGHSW97IJjTbElEKYWHy3Vb0OjpB0Kk7eIbJJsNTsgb4"
username = "lokeshpatil1105"
api_key = "67d5ddf5bdb798ee6342f0372b3efcd1"

# compressing all the user authentications into one object variable 
shop_keeper = veryfi.Client(shop_keeper_id, shop_keeper_secret, username, api_key)

total="total"
grand_total=0

# calling the api on each product image
for tag in prod_list:
    tag_ = shop_keeper.process_document(tag)
    cost_of_prod = tag_[total]
    print(tag,' : ',cost_of_prod)
    grand_total+=cost_of_prod

master = Tk()
x = grand_total #assigned to variable x like you showed
master.minsize(width=400, height=400)
w = Label(master, font=("Calibri",42,"bold"),text="BELLA")
v = Label(master, font=("Calibri",36,"bold"),text="Your Grand total is: ")
y = Label(master, font=("Calibri",36,"bold"),text=x) #shows as text in the window

w.pack() #organizes widgets in blocks before placing them in the parent.          
v.pack()
y.pack()
mainloop()




