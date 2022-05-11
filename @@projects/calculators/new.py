from tkinter import *
root=Tk()
root.geometry("400x300")
# x=10
y=10


for i in range(2):
    x=10
    for j in range(3):
        b=Button(root,text="arnab").place(x=x,y=y)
        x+=50
    y+=50
root.mainloop()