#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

abcdario='abcdefghijklmnñopqrstuvwxyz'

def gen(largo):
	a = ''
	for letra in range(0, largo):
		var = random.randrange(3)
		if 0 == var:
			a += abcdario[random.randrange(26)]
		elif 1 == var:
			a += abcdario[random.randrange(26)].upper()
		else:
			a += str(random.randrange(9))
	return(a)

elecc = input('numero de caracteres --> ')
print(gen(int(elecc)))
