from tkinter import *
import webbrowser as gb

class githuButton(Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.pySefiGUI()

	def pySefiGUI(self):
		self.myGh = Frame(self, bg="black")
		self.myGh.pack(expand=True,fill='both')

		self.l2 = Label(self.myGh, text="☆developmentMen☆",
                bg="black",fg="white").pack()
		self.photo = PhotoImage(file=r"baner.png").subsample(
		20,23)
		self.ghButon = Button(self.myGh,highlightthickness=0,
		text="Check my GitHub --->",
		anchor="center",bg="black",activebackground=
		"black",relief="flat",borderwidth=0,activeforeground=
		"white",width=250,command=self.gitHub,
		fg="white",image=self.photo,compound="right"
		).pack()
	def gitHub(self):
                gb.open("https://github.com/developmentMen")

r = Tk()
r.wm_title("check my GitHub")
app = githuButton(r)
app.mainloop()
