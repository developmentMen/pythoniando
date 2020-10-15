'''
        Sockets TCP programado para recibir un mensaje
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((input("ingrese ip a conectar -->"), 64444))

datos = s.recv(1024)

print(datos.decode())

s.close()
