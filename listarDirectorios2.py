#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

cont = 1
dirs = []

print("\nElegir archivos:\n")

for e in os.scandir(os.getcwd()):
	dirs.append(e.name)
	print("	[{}] - {}".format(cont, e.name))
	cont += 1

print("\n\t\t\tpress (q) for quit.\n")

while True:
	eleccion = input("eleccion --> ")
	if eleccion == "q": break;

	print(dirs[int(eleccion)-1])
