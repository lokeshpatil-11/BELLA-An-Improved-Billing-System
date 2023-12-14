from tkinter import *

grand_total =100

master = Tk()
x = grand_total #assigned to variable x like you showed
master.minsize(width=400, height=400)
w = Label(master, font=("Bodoni MT Black",42,"bold"),text="BELLA")
v = Label(master, font=("Calibri",36,"bold"),text="Your Grand total is: ")
y = Label(master, font=("Calibri",36,"bold"),text=x) #shows as text in the window
 
w.pack() #organizes widgets in blocks before placing them in the parent.          
v.pack()
y.pack()
mainloop()
