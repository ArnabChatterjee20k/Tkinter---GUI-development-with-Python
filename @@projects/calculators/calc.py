import math
import tkinter as tk

w=tk.Tk()
w.title("Calculator---Coded by Arnab Chatterjee")
w.configure(background="black")
w.geometry("500x500")
w.resizable(False,False)
x=tk.StringVar()
expression=""

def press(n):
    global expression
    expression =expression+str(n)
    x.set(expression)
    return expression
def clear():
    global expression

    x.set("")

    expression = ""
    return expression
def back():
    global expression
    a=len(expression)-1
    c=expression[:a]
    expression=c
    x.set(c)
    return expression
def equal():
    global expression
    total=str(eval(expression))
    x.set(total)
    expression=(total)
    x.set(expression)
    return expression

def factorial():
    global expression
    a=math.factorial(int(expression))

    a=str(a)
    x.set(a)
    expression=a
    return(expression)

def cos():
    global expression
    
    expression=math.cos(math.radians(int(expression)))
    x.set(expression)
    return(expression)

def sin():
    
    global expression
    
    expression=math.sin(math.radians(int(expression)))
    x.set(expression)
    return(expression)

def tan():
    global expression
    
    expression=math.tan(math.radians(int(expression)))
    x.set(expression)
    return(expression)


e1=tk.Entry(w,justify="right",borderwidth="10",font=("","20","bold"),textvariable=x)
e1.place(x=0,y=0,width="500",height="60")

b1=tk.Button(w,text="1",font=("","20"),bg="grey",fg="black",activeforeground="black")
b1.place(x=0,y=70,width="70",height="70")
b1.bind("<Enter>",lambda e: b1.configure(background="white"))
b1.bind("<Leave>",lambda e: b1.configure(background="Grey"))
b1.configure( command= lambda:press(1))

b2=tk.Button(w,text="2",font=("","20"),bg="grey",fg="black",activeforeground="black")
b2.place(x=80,y=70,width="70",height="70")
b2.bind("<Enter>",lambda e: b2.configure(background="white"))
b2.bind("<Leave>",lambda e: b2.configure(background="Grey"))
b2.configure( command= lambda:press(2))

b3=tk.Button(w,text="3",font=("","20"),bg="grey",fg="black",activeforeground="black")
b3.place(x=160,y=70,width="70",height="70")
b3.bind("<Enter>",lambda e: b3.configure(background="white"))
b3.bind("<Leave>",lambda e: b3.configure(background="Grey"))
b3.configure( command= lambda:press(3))

b4=tk.Button(w,text="4",font=("","20"),bg="grey",fg="black",activeforeground="black")
b4.place(x=0,y=150,width="70",height="70")
b4.bind("<Enter>",lambda e: b4.configure(background="white"))
b4.bind("<Leave>",lambda e: b4.configure(background="Grey"))
b4.configure( command= lambda:press(4))

b5=tk.Button(w,text="5",font=("","20"),bg="grey",fg="black",activeforeground="black")
b5.place(x=80,y=150,width="70",height="70")
b5.bind("<Enter>",lambda e: b5.configure(background="white"))
b5.bind("<Leave>",lambda e: b5.configure(background="Grey"))
b5.configure( command= lambda:press(5))

b6=tk.Button(w,text="6",font=("","20"),bg="grey",fg="black",activeforeground="black")
b6.place(x=160,y=150,width="70",height="70")
b6.bind("<Enter>",lambda e: b6.configure(background="white"))
b6.bind("<Leave>",lambda e: b6.configure(background="Grey"))
b6.configure( command= lambda:press(6))

b7=tk.Button(w,text="7",font=("","20"),bg="grey",fg="black",activeforeground="black")
b7.place(x=0,y=230,width="70",height="70")
b7.bind("<Enter>",lambda e: b7.configure(background="white"))
b7.bind("<Leave>",lambda e: b7.configure(background="Grey"))
b7.configure( command= lambda:press(7))
b7.configure( command= lambda:press(7))

b8=tk.Button(w,text="8",font=("","20"),bg="grey",fg="black",activeforeground="black")
b8.place(x=80,y=230,width="70",height="70")
b8.bind("<Enter>",lambda e: b8.configure(background="white"))
b8.bind("<Leave>",lambda e: b8.configure(background="Grey"))
b8.configure( command= lambda:press(8))
b8.configure( command= lambda:press(8))

b9=tk.Button(w,text="9",font=("","20"),bg="grey",fg="black",activeforeground="black")
b9.place(x=160,y=230,width="70",height="70")
b9.bind("<Enter>",lambda e: b9.configure(background="white"))
b9.bind("<Leave>",lambda e: b9.configure(background="Grey"))
b9.configure( command= lambda:press(9))
b9.configure( command= lambda:press(9))

b9=tk.Button(w,text="9",font=("","20"),bg="grey",fg="black",activeforeground="black")
b9.place(x=160,y=230,width="70",height="70")
b9.bind("<Enter>",lambda e: b9.configure(background="white"))
b9.bind("<Leave>",lambda e: b9.configure(background="Grey"))
b9.configure( command= lambda:press(9))


bk=tk.Button(w,text="back",font=("","20"),bg="grey",fg="black",activeforeground="black")
bk.place(x=240,y=70,width="70",height="70")
bk.bind("<Enter>",lambda e: bk.configure(background="white"))
bk.bind("<Leave>",lambda e: bk.configure(background="Grey"))
bk.configure( command=lambda :back())

bc=tk.Button(w,text="C",font=("","20"),bg="grey",fg="black",activeforeground="black")
bc.place(x=240,y=150,width="70",height="70")
bc.bind("<Enter>",lambda e: bc.configure(background="white"))
bc.bind("<Leave>",lambda e: bc.configure(background="Grey"))
bc.configure( command=clear)

be=tk.Button(w,text="=",font=("","20"),bg="grey",fg="black",activeforeground="black")
be.place(x=240,y=230,width="70",height="70")
be.bind("<Enter>",lambda e: be.configure(background="white"))
be.bind("<Leave>",lambda e: be.configure(background="Grey"))
be.configure( command=equal)

bp=tk.Button(w,text="+",font=("","20"),bg="grey",fg="black",activeforeground="black")
bp.place(x=0,y=310,width="70",height="70")
bp.bind("<Enter>",lambda e: bp.configure(background="white"))
bp.bind("<Leave>",lambda e: bp.configure(background="Grey"))
bp.configure(command= lambda:press("+"))

bm=tk.Button(w,text="-",font=("","20"),bg="grey",fg="black",activeforeground="black")
bm.place(x=80,y=310,width="70",height="70")
bm.bind("<Enter>",lambda e: bm.configure(background="white"))
bm.bind("<Leave>",lambda e: bm.configure(background="Grey"))
bm.configure(command= lambda:press("-"))

bmu=tk.Button(w,text="*",font=("","20"),bg="grey",fg="black",activeforeground="black")
bmu.place(x=160,y=310,width="70",height="70")
bmu.bind("<Enter>",lambda e: bmu.configure(background="white"))
bmu.bind("<Leave>",lambda e: bmu.configure(background="Grey"))
bmu.configure(command= lambda:press("*"))

bd=tk.Button(w,text="/",font=("","20"),bg="grey",fg="black",activeforeground="black")
bd.place(x=240,y=310,width="70",height="70")
bd.bind("<Enter>",lambda e: bd.configure(background="white"))
bd.bind("<Leave>",lambda e: bd.configure(background="Grey"))
bd.configure(command= lambda:press("/"))

bf=tk.Button(w,text="!" ,font=("","20"),bg="grey",fg="black",activeforeground="black")
bf.place(x=320,y=310,width="70",height="70")
bf.bind("<Enter>",lambda e: bf.configure(background="white"))
bf.bind("<Leave>",lambda e: bf.configure(background="Grey"))
bf.configure(command=factorial)

b0=tk.Button(w,text="0",font=("","20"),bg="grey",fg="black",activeforeground="black")
b0.place(x=80,y=380,width="70",height="70")
b0.bind("<Enter>",lambda e: b0.configure(background="white"))
b0.bind("<Leave>",lambda e: b0.configure(background="Grey"))
b0.configure( command= lambda:press(0))
b0.configure( command= lambda:press(0))

bsin=tk.Button(w,text="sin" ,font=("","20"),bg="grey",fg="black",activeforeground="black")
bsin.place(x=320,y=70,width="70",height="70")
bsin.bind("<Enter>",lambda e: bsin.configure(background="white"))
bsin.bind("<Leave>",lambda e: bsin.configure(background="Grey"))
bsin.configure(command=sin)

bcos=tk.Button(w,text="cos" ,font=("","20"),bg="grey",fg="black",activeforeground="black")
bcos.place(x=320,y=150,width="70",height="70")
bcos.bind("<Enter>",lambda e: bcos.configure(background="white"))
bcos.bind("<Leave>",lambda e: bcos.configure(background="Grey"))
bcos.configure(command=cos)


btan=tk.Button(w,text="tan" ,font=("","20"),bg="grey",fg="black",activeforeground="black")
btan.place(x=320,y=230,width="70",height="70")
btan.bind("<Enter>",lambda e: btan.configure(background="white"))
btan.bind("<Leave>",lambda e: btan.configure(background="Grey"))
btan.configure(command=tan)

w.mainloop()
intro=tk.Tk()
intro.title("Calculator credits")
intro.geometry("500x500")

new=tk.Label(intro,text='Coded bY\n\n Arnab Chatterjee\n\nclass:XI-Sc\n\nROll:7',font="Courier 30 bold italic",bg="red",fg="yellow").place(x=60,y=100)
intro.mainloop()