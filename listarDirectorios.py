import os

a	 = os.scandir(os.getcwd())
cont = 1

for e in a:
	print("[{}] - {}".format(cont, e.name))
	cont ++