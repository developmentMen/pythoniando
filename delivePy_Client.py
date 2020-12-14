import socket

s = socket.socket()

host = input("ingrese la ip del servidor -->")

s.connect((host, 6333))
print("connected...")

datos = s.recv(1024)

filename = datos.decode()
file = open(filename, 'wb')
fileData = s.recv(1024)
file.write(fileData)
file.close()
print('archivo recibido.')
