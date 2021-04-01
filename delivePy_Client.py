#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

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
	print('archivo recibido.')

def main():
	s = socket.socket()
	host = input("ingrese la ip del servidor -->")
	s.connect((host, 6333))
	try:
		while True:
			recibir(s)
	except :
		pass

	s.close()


if __name__=='__main__':
	main()
