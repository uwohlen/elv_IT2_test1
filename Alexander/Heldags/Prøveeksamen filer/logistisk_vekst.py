import numpy as np
import matplotlib.pyplot as plt

# Konstanter for en logistisk funksjon:
# f(x) = C / ( 1 + ae^-bx )
a = 20
b = 0.1
C = 50

# Konstanter for løsningen
antall_forslag = 100 # antall løsninger vi tester parallelt
behold = 10 # antall løsninger vi beholder fra hver generasjon, max lik antall_forslag

grense = 1000 # startverdier for x er innenfor [-grense,grense> når vi bruker np.random.uniform(fra,til,antall)
maal = 9999 # 1 / nøyaktighet

utskrift = 1 # antall linjer skrevet pr generasjon
generasjoner = 1000 # antall runder med mutasjoner før vi gir oss, hvis vi ikke får ønsket nøyaktighet

def f(x,a,b,C):
    """
    Logistisk funksjon
    """
    ebx = np.e**(-b*x)
    return C/(1+a*ebx)

# Sjekk grafen for funksjonen
xverdier = np.linspace(-grense,grense,1001)

def fig(funk,tittel):
    plt.grid(True)
    plt.axhline(y=0, xmin=0, xmax=1,color="black")
    plt.axhline(y=C/2, xmin=0, xmax=1,color="blue")
    plt.axvline(x=0, ymin=0, ymax=1,color="black")
    plt.axvline(x=np.log(a)/b, ymin=0, ymax=1,color="blue")
    plt.title(tittel)
    plt.plot(xverdier,funk,"r")
    plt.show()

#fig(f(xverdier,a,b,C),"Funksjonen")

# Hvor god er foreslått løsning?
def finnXfraY(x,a,b,C):
    ans = f(x,a,b,C) - C/2
    if ans == 0:
        return 999999
    else:
        return float(abs(1/ans))

# Gjett y-verdier
forslag = np.random.uniform(-grense,grense,antall_forslag)

# Finn beste løsning
for i in range(generasjoner):
    sorterte_forslag = []
    for x in forslag:
        passer = finnXfraY(x,a,b,C)
        sorterte_forslag.append((passer,x))

    sorterte_forslag.sort()
    sorterte_forslag.reverse()

    #for j in range(utskrift):
    #    print(sorterte_forslag[j])

    if sorterte_forslag[0][0] >= maal:
        break

    beste = []
    for k in range(behold):
        beste.append(sorterte_forslag[k][1])

# Skriv ut beste løsning
print(i,round(sorterte_forslag[0][1],3), round(f(sorterte_forslag[0][1],a,b,C),3))