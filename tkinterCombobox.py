from tkinter import *
from tkinter import ttk

#help(ttk.Combobox())

ventanaRaiz = Tk()
ventanaRaiz.title("Combobox con Tkinter")

bannerText =  """
test Combobox.Py
"""
banner = Label(ventanaRaiz, text=bannerText,font="Times 23 italic").grid(column=0, row=0,columnspan=2)

opciones = ttk.Combobox(ventanaRaiz, values=["all", 'name','pass','strong Pass'])
opciones.current(0)
opciones.grid(column=0, row=2)

lab = Label(ventanaRaiz, text="Type",width=20, height=3).grid(column=0, row=1)

salida = Label(ventanaRaiz, text="as")
salida.grid(column=0, row=4)

def gen():
	#t = opciones.get()
	salida["text"] = opciones.get()

bot = Button(ventanaRaiz, text="generate", font=" , 10", command=gen).grid(column=1, row=3)

#opciones.pack()
#opciones.grid(column=0, row=1)
footerText='--> by DevelopmentMen '
footer = Label(ventanaRaiz, text=footerText, font="Helvetica 10 italic").grid(column=1,row=4)

ventanaRaiz.mainloop()
