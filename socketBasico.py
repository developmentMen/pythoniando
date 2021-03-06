#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	Sockets TCP programado para dar un mensaje
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#se crea un socket TCP
s.bind((socket.gethostname(), 64444))
	#se elige el puerto
s.listen()

try:
	while True:
		conn, addr = s.accept()
		#acepta la coneccion y devuelve el socket (conn)
		#y la direccion ip (addr)

		print('Conectado con --->', addr)
		mensaje = "mensaje enviado desde el server\n"
		conn.send(mensaje.encode())
		conn.close()

except KeyboardInterrupt:
	s.close()
