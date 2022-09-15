from pylab import *

liste = ['a', 'b', 'c', 'd', 1]
liste2 = ['d', 'e', 'f', 'g', 2]

if 'e' in liste:
    print('fant')
    
else:
    print('fant ikke')
    
if 'd' in liste or 'd' in liste2:
    print('korrekt')

else:
    print('ikke korrekt')


liste.insert(3,3)

liste.extend(liste2)
  