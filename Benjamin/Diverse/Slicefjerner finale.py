# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:06:25 2022

@author: bespa
"""

q = [1, 2, 3, 4, 5, 6]
a = [3, 5, 2, 4, 77, 5]


def slicefjerner(slicestart, sliceslutt, liste):
    """Denne funksjonen fjerner en bestemt slice fra en liste og returnerer den tilbake,
    hvor første argument er start index til slicen og andre parameter er slutt indexen til slicen.
    Det tredje og siste argumentet er navn på listen du skal fjerne fra. Husk at første index er 0 i listen din"""
    
    for i in range(slicestart, sliceslutt + 1):
        liste.pop(slicestart)
    return liste


print(slicefjerner(2, 4, q))   #Skriv inn slicen du vil fjerne, 
                               #og navnet på listen i argumentet til slicefjerner funksjonen
