"""
	|Python File Sender|

programa simple para enviar archivos
"""
import socket
import sys

def enviar(sock, filename):
	sock.send(filename.encode())

	file = open(filename,'rb')
	while True:
		strng = file.readline(512)
		if not strng:
			break
		sock.send(strng)
	file.close()
	print("archivo enviado con exito")

def main():
	s = socket.socket()

	s.connect((sys.argv[1], 6333))
	#try:
	while True:
		enviar(s, sys.argv[2])
	#except :
	#	pass

	s.close()


if __name__=='__main__':
	main()