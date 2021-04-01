#!/bin/bash
#======================
#Script para crear un nuevo archivo Python listo para codear

echo "#!/usr/bin/env python3" > $1
echo "# -*- coding: utf-8 -*-" >> $1
echo "# =============================" >> $1
echo "# Author	--> " >> $1
echo "# Date created	--> XX/XX/2021" >> $1
echo "# Last modified	--> XX/XX/2021" >> $1
echo "# Version	--> $(python3 -V)" >> $1
echo "# =============================" >> $1
echo "'''" >> $1
echo " este programa fue echo para..." >> $1
echo "'''" >> $1
echo "# =============================" >> $1
echo "# Imports" >> $1
echo "" >> $1
echo "# =============================" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "if __name__ == '__main__':" >> $1
echo "	" >> $1

nano $1

