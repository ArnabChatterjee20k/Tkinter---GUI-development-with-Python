import tkinter as tk
import os
from tkinter.constants import TOP
from PIL import Image, ImageTk #since I have jpg images

root=tk.Tk()
root.title("Album")
root.geometry("300x300")
#directory
directory="images/"
img_directory=os.listdir(directory)
# print(directory+img_directory[0])
#functions
current_img=0
def next_img():
    #TODO: next image function
    global current_img,image
    current_img+=1
    if current_img==len(img_directory)-1:
        b_next.configure(state='disabled')
    print(directory+img_directory[current_img])
    image=Image.open(directory+img_directory[current_img])
    image=ImageTk.PhotoImage(image)
    lab.configure(image=image)
    return current_img,image

def prev_img():
    #TODO: previous image function
    global current_img,image
    current_img-=1
    if current_img==0:
        b_prev.configure(state='disabled')
    print(directory+img_directory[current_img])
    image=Image.open(directory+img_directory[current_img])
    image=ImageTk.PhotoImage(image)
    lab.configure(image=image)
    return current_img,image

#img coordinates
x=100
y=100
#Buttons
b_next=tk.Button(root,text=">>",command=next_img)
b_next.pack()
b_prev=tk.Button(root,text="<<",command=prev_img)
b_prev.pack()
#Labels
image=Image.open(directory+img_directory[current_img])
image=ImageTk.PhotoImage(image)
lab=tk.Label(root,image=image)
lab.place(x=x,y=y)


root.mainloop()