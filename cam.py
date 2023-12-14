import cv2

cam = cv2.VideoCapture(0)


    
def capture_frame(cam,k):
    cv2.namedWindow("Python Webcam Screenshot App")
    img_counter = 0
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
        img_counter +=1        
    cam.release()    
    cam.destroyAllWindows()
    
capture_frame(cam)