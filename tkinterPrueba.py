from tkinter import *

v = Tk()

l = Label(v,text="hola")
l.pack()

l2 = Label(v, text="test",width=10)
l2.pack()

b = Button(v, text="button",).pack(expand=True,fill="both")
v.mainloop()
