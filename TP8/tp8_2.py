#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:35:52 2022

@author: noedaniel
"""

"""Question 7 et 8"""

def guerrier_glorieux(nom_fichier):
    f = open(nom_fichier, 'w')
    f.writelines("for k in range(10):\n")
    f.writelines('   print("RIP")')
    f.close()
    
"""Question 9"""

import sys 

print(sys.argv[0])