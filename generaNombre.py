#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def nombre():
    n = random.randint(1,3)
    s = "";

    for i in range(n): # silabas
        s += CONSONANTS[random.randint(0,len(CONSONANTS)-1)]
        s += VOWELS[random.randint(0,len(VOWELS)-1)]
        if i==n-1 and random.randint(0,1)==0 : s += CONSONANTS[random.randint(0,len(CONSONANTS)-1)]

    return s

for x in range(20): print(nombre())
