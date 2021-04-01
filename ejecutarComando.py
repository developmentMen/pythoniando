#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import check_output
import sys, codecs


info = check_output("python mostrarIp.py", shell=True).decode('utf-8')
#deco = info.decode('utf8')
print(info)
