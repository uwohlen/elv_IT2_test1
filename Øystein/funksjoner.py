"""
Created by: Øystein
"""

import typing

def gjennomsnitt(liste: list[int | float]) -> int | float:
    """
    gjennomsnitt regner ut gjennomsnittet av tallene i listen.
    """
    if len(liste) == 0:
        return 0
    return sum(liste)/len(liste)


def median(liste: list[int | float]) -> int | float:
    """
    median regner ut medianen av tallene i listen.
    """
    if len(liste) == 0:
        return 0
    liste.sort()
    if len(liste) % 2 == 0:
        return (liste[len(liste)//2-1] + liste[len(liste)//2])/2
    return liste[len(liste)//2]


def typetall(liste: list[typing.Any]) -> tuple[typing.Any, int]:
    """
    typetall returner elementet med høyest forekomst.
    I tillegg returnerer funksjonen antall forekomster av elementet.
    Funksjonen fungerer på alle elementtyper, ikke bare tall.
    """
    antall = {}
    rekord = 0
    rekord_element = None
    for element in liste:
        if antall.get(element) == None:
            antall[element] = 1
        else:
            antall[element] += 1
        if antall[element] > rekord:
            rekord = antall[element]
            rekord_element = element
    return rekord_element, rekord


def rekursiv_sortering(liste: list):
    """
    rekursiv_sortering leter etter lister i listen rekursivt, 
    og sorterer listen hvis den ikke inneholder flere lister.
    """
    if len(liste) == 0:
        return
    if type(liste[0]) != list:
        liste.sort()
        return
    for element in liste:
        rekursiv_sortering(element)
