import tkinter

class TestPoo(tkinter.Frame):

	def __init__(self, master=None):
		super().__init__(master, width=320, height=170)
		self.master = master
		self.pack()
		self.unBoton()

	def unBoton(self):
		self.b1 = tkinter.Button(self, text="Exit\nButton", fg="red",command=exit).grid(column=1,row=0,padx=50)

r = tkinter.Tk()
r.wm_title("soy el titulo")
app = TestPoo(r)
app.mainloop()
