"""
	|Python File Sender|

programa simple para enviar archivos
"""
import socket
import sys
import time

def enviar(s, filename):
	s.send(filename.encode())
	time.sleep(1)
	file = open(filename, 'rb')
	while True:
		strng = file.readline(512)
		if not strng:
			break
		s.send(strng)
	file.close()
	print("archivo enviado con exito")

def main():
	s = socket.socket()
	s.connect((sys.argv[1], 6333))
	#try:
	enviar(s, sys.argv[2])
	#except :
		#print("an error was ocurred")
		#pass

	s.close()


if __name__=='__main__':
	main()