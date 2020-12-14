import os
import socket 

s = socket.socket()

s.bind((socket.gethostname(), 6333))
s.listen(3)
print("servidor esperando --> {}".format(socket.gethostbyname(socket.gethostname())))
con, addr = s.accept()

#	se conecta

print(addr, "se conecto")

cont = 1
dirs = []

print("\nElegir archivos:\n")

for e in os.scandir(os.getcwd()):
	dirs.append(e.name)
	print("	[{}] - {}".format(cont, e.name))
	cont += 1

print("\n\t\t\tpress (q) for quit.\n")

filename = dirs[int(input("Archivo a enviar: "))-1]

#	archivo elegido

con.send(filename.encode())


file = open(filename, 'rb')
fileContent = file.read(1024)
con.send(fileContent)
file.close()
print("archivo enviado con etsito")

con.close()
s.close()
