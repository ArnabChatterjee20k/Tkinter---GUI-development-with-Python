
from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
# can_widget.pack()
# bd: It defines the border width in pixels. The default value is 2.
# bg: Normal background color.
# height: It defines the size of the canvas in the Y dimension.
# width: It defines the size of the canvas in the X-direction.
# relief: It specifies the type of border. Some of the values are SUNKEN, RAISED, GROOVE, and RIDGE.

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

can_widget.create_text(200, 200, text="python")

#provide coordinates of a rectangle
can_widget.create_oval(344,233,244,355)


root.mainloop()

