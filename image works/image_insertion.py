
from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("1255x944")
# photo = PhotoImage(file="1.png") #we dont require PIL to do this.Insert it in the label to show. This is available in Tkinter itself.But it doesnot support jpg
#So we require PIL

# For Jpg Images

image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()



mahmudul_root.mainloop()


# TK.PhotoImage==Not support for jpg
# PIL.PhotoImage== jpg