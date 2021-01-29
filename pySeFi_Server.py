"""
	|Python File Sender|

programa simple para enviar archivos
"""
import socket
import sys

def conectar(s):
	con, addr = s.accept()
	print(addr, "se conecto")

	return con

def recibir(s):
	datos = s.recv(1024)
	filename = datos.decode()

	file = open(filename, 'wb')
	while True:
		fileData = s.recv(512)
		if not fileData:
			break
		file.write(fileData)
	file.close()
	print('archivo recibido {}.'.format(filename))

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
			recibir(s)
	except :
		pass

	cerrar(con, s)

if __name__=='__main__':
	main()