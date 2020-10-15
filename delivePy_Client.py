import socket

s = socket.socket()

host = input("ingrese la ip del servidor -->")

s.connect((host, 64444))
print("connected...")

filename = input("nombre para el nuevo archivo")
file = open(filename, 'wb')
fileData = s.recv(1024)
file.write(fileData)
file.close()
print('archivo recibido.')
