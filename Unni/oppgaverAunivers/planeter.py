"""
Viser import av felles fil med klasser, relativ adresse opp og ned i mapper
UW
"""

# fortell python om hvor filene ligger
import sys, os
#print("Mappestruktur besteforelder: ",os.path.dirname(os.path.dirname(sys.path[0])))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(sys.path[0])),"felles"))

#import klassebibAuni as kbib
#jupiter = kbib.Planet("Jupiter",778.5,69911)

from klassebibAuni import Planet
#help(Planet)

merkur = Planet("Merkur", 57.91, 2439.7)
venus = Planet("Venus", 108.2, 6051.8)
jorda = Planet("Jorda", 149.6, 6371)
mars = Planet("Mars", 227.9, 3389.5)
jupiter = Planet("Jupiter", 778.5, 69911, 4)
#ringer: jupiter 4, saturn 7, uranus 13, neptun 6

planetene = [merkur, venus, jorda, mars, jupiter]

#for i in range(len(planetene)):
  #print(planetene[i].navn, planetene[i].volum())
  

print(type(jorda))
print(jorda)
print(vars(jorda))