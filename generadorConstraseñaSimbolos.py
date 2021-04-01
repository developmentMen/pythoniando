#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

abcdario='abcdefghijklmnñopqrstuvwxyz'
simbolos = '¡?=)(/&%$#"!°|*[]-_,;.'

def gen(largo):
	a = ''
	for letra in range(0, largo):
		var = random.randrange(4)
		if 0 == var:
			a += abcdario[random.randrange(26)]
		elif 1 == var:
			a += abcdario[random.randrange(26)].upper()
		elif 2 == var:
			a += simbolos[random.randrange(21)]
		else:
			a += str(random.randrange(9))
	return(a)

elecc = input('numero de caracteres --> ')
print(gen(int(elecc)))
