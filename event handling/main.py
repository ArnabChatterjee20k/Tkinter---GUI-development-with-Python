from tkinter import *

def harry(event):#bind automatically passes a object so we have to use event in function just like js
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text='Click me please')
widget.pack()

widget.bind('', harry)
widget.bind('', quit)

root.mainloop()
# we can get more events in google search