# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:04:55 2022

@author: jasea001
"""


def Convert(string, op):
    li = list(string.split(op))
    return li

stykke = str(input("skriv et regnestykke "))

if "+" in stykke:
    tall = Convert(stykke,"+")
    sum = float(tall[0]) + float(tall[1])
else:
    tall = Convert(stykke,"-")
    sum = float(tall[0]) - float(tall[1])

print(sum)