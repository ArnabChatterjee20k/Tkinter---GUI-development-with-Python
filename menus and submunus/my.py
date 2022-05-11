from tkinter import *

root=Tk()

mainmenu=Menu(root)

file=Menu(mainmenu)
file.add_cascade(label="Arnab")
file.add_separator()
file.add_cascade(label="Bittu")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=file)


Edit=Menu(mainmenu,tearoff=20)
Edit.add_cascade(label="Arnab")
Edit.add_separator()
Edit.add_cascade(label="Bittu")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=Edit)

root.mainloop()