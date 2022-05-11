from tkinter import *

root=Tk()
root.geometry("500x500")
font=("times 15 bold")

def opr():
    with open("data.txt","a+") as file:
        file.write(f"{e1.get()} {e2.get()} {slide.get()}")
    return

name=Label(root,text="Name",font=font).grid(row=0,column=0,pady=25)
food=Label(root,text="Food Ordered",font=font).grid(row=1,column=0,pady=10,padx=10)

# var1=StringVar()
# var2=StringVar()
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)

Label(root,text="Review").grid(row=2,column=0)
slide=Scale(root,from_=1,to=5,tickinterval=1,orient=HORIZONTAL)
slide.grid(row=2,column=1)
slide.set(5)
# btn=Button(root,text="Submit",padx=10,pady=10,command=lambda:print(e1.get())
btn=Button(root,text="Submit",padx=10,pady=10,command=opr)
btn.grid(row=3,column=0)
btn.bind("<Enter>",lambda event:btn.config(fg="red")) #e since bind by default return event object
btn.bind("<Leave>",lambda event:btn.config(fg="black")) #e since bind by default return event object
root.mainloop()