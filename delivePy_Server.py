import os
import socket 

def conectar(s):
	con, addr = s.accept()
	print(addr, "se conecto")

	return con

def menu():
	cont = 1
	dirs = []

	print("\nElegir archivos:\n")
	for e in os.scandir(os.getcwd()):
		dirs.append(e.name)
		print("	[{}] - {}".format(cont, e.name))
		cont += 1
	print("\n\t\t\tpress (q) for quit.\n")

	eleccion = input("Archivo a enviar --> ")
	filename = dirs[int(eleccion)-1]

	return filename

def enviar(con, filename):
	con.send(filename.encode())

	file = open(filename,'rb')
	while True:
		strng = file.readline(512)
		if not strng:
			break
		client_socket.send(strng)
	file.close()
	print("archivo enviado con exito")


'''
def enviar(con, filename):
	con.send(filename.encode())

	file = open(filename, 'rb')
	fileContent = file.read(1024)
	con.send(fileContent)
	file.close()
	print("archivo enviado con etsito")
'''

def cerrar(con, s):
	con.close()
	s.close()

def main():
	s = socket.socket()

	s.bind((socket.gethostname(), 6333))
	s.listen()
	print("servidor esperando --> {}".format(socket.gethostbyname(socket.gethostname())))
	con = conectar(s)
	try:
		while True:
			enviar(con, menu())
	except :
		pass
	
	cerrar(con, s)

if __name__=='__main__':
	main()