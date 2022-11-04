import sys as sys
import time
import random as r

def sistenummer(inum:int) -> int:
    """Finner det siste sifferet i ett nummer"""
    sinum = str(inum)
    ssinum = sinum[-1]
    return int(ssinum)

def indekssiffer(inum:float) -> float:
    """Finner inkekssifferet til ett nummer. Input kan enten være float eller int"""
    iinum = str(inum)
    iiinum = iinum[0]
    return int(iiinum)



def median(liste):
    """Finner medianen til en liste"""
    par = [0,2,4,6,8]

    if (sistenummer(len(liste)) in par):
        return (liste[int(len(liste)/2)] + liste[int((len(liste)/2)-1)])/2

    elif (sistenummer(len(liste)) not in par):
        return liste[int(len(liste)/2)]


def split(iliste:list,o) -> tuple:
    """Splitter en liste til 2 tekst-strenger. Tar en liste, og ett element listen skal splittes rundt."""
    # gjøre om listen inn, til en liste med strings
    liste = []
    for i in range(len(iliste)):
        liste.append(str(iliste[i]))


    vs = str()
    hs = str()
    funnet = False

    for i in range(1,len(liste)): #finne operatoren, og poisjonen til operatoren. Hopper over første operator for å kunne regne med negative tall
        if liste[i] == str(o):
            p = i
            funnet = True
            break

    if funnet == False:
        sys.exit("Tegnet som skal splittes rundt, ble ikke funnet i stringen")
    

    for i in range(p): #finne hva som er på venstre side av operatoren
        vs = vs + liste[i]
    for i in range(p+1,len(liste)): #finne hva som er på høyre side av operatoren
        hs = hs + liste[i]
    return (vs,hs)

def slow_type(t):
    typing_speed = 300 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(r.random()*10.0/typing_speed)

def slower_type(t,speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()







