import tkinter

r = tkinter.Tk()
r.geometry("200x100")

a = tkinter.Frame(r, bg="blue")
a.pack(expand=True,fill='both')

b = tkinter.Frame(r, bg="black",cursor="heart")
b.pack(expand=True,fill='both')

l= tkinter.Label(a, text="hola",justify="right").grid(column=0,row=0,
	sticky="w")
b = tkinter.Button(a, text="Red", fg="red").grid(column=1,row=0,padx=50)
b1= tkinter.Button(b ,text="balablb",fg="black").pack()
r.mainloop()
