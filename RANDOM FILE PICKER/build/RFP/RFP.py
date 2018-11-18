#Importing necessary Packages & Libraries
import os, random, shutil, datetime, sys
from tkinter import *

#RFP function for choosing random files
def RFP():
    
    #Variable for getting the value from textfield
    no_of_files=value.get()
    source=src.get()
    destination=dest.get()
    
    #Using for loop to randomly choose multiple files
    for i in range(no_of_files):
        #Variable "random_file" stores the name of the random file chosen
        random_file=random.choice(os.listdir(source))
        file="%s\%s"%(source,random_file) 
        #"shutil.move" function moves file from one directory to another
        shutil.move(file,destination)

    Display=Label(root, text="File Transfer Successful !!!")
    Display.config(font=("Calibri",15))
    Display.grid(row=7,column=1 ,sticky=W)

#Creating GUI Frame along with Frame Title
root = Tk()
root.title("Random File Picker Application")
root.wm_iconbitmap('D:\PYTHON CREATIVE-SPACE\PROJECTS\RANDOM FILE PICKER\RESOURCES\RFP ICON_MAIN.ico')
value = IntVar()
src=StringVar()
dest=StringVar()

#Creating Widgets and Button
label=Label(root, text="Enter no of files : ")
label.grid(row=1,column=1 ,sticky=W)
label.config(font=("Calibri",20))
entry=Entry(root, textvariable = value)
entry.grid(row=1, column=5, sticky=E)
entry.config(font=("Calibri",15))

label=Label(root, text="Enter Source Directory : ")
label.grid(row=2,column=1 ,sticky=W)
label.config(font=("Calibri",20))
entry=Entry(root, textvariable = src)
entry.grid(row=2, column=5, sticky=E)
entry.config(font=("Calibri",15))

label=Label(root, text="Enter Destination Directory : ")
label.grid(row=3,column=1 ,sticky=W)
label.config(font=("Calibri",20))
entry=Entry(root, textvariable = dest)
entry.grid(row=3, column=5, sticky=E)
entry.config(font=("Calibri",15))

Select = Button(root, text="Transfer Files", command=RFP)
Select.grid(row=5, column=1,sticky=W)
Select.config(font=("Calibri",17))

root.mainloop()
