import socket 

s = socket.socket()

s.bind((socket.gethostname(), 64444))
s.listen(1)
print("servidor esperando --> {}".format(socket.gethostname()))
con, addr = s.accept()

print(addr, "se conecto")
filename = input("nombre del archivo a enviar: ")
file = open(filename, 'rb')
fileContent = file.read(1024)
con.send(fileContent)
file.close()
print("archivo enviado con etsito")

con.close()
s.close()
