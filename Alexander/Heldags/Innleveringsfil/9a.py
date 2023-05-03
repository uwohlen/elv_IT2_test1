import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("roboter.csv", delimiter=';', encoding = "ISO-8859-1")

syssel = list(file["sysselsette"])
næring = list(file["næring"])
industri18 = list(file["Industrirobotar_2018"])
industri20 = list(file["Industrirobotar_2020"])
industri22 = list(file["Industrirobotar_2022"])

teneste18 = list(file["Tenesterobotar_2018"])
teneste20 = list(file["Tenesterobotar_2020"])
teneste22 = list(file["Tenesterobotar_2022"])

sammensatt = []
for x in range(len(syssel)):
    sammensatt.append((syssel[x], næring[x],industri22[x], teneste22[x]))
    
def hent(index, value, lst):
    ret = []
    for i in range(len(lst)):
        if lst[i][index] == value:
            ret.append(lst[i])
            
    return ret

over100 = hent(0, "100 sysselsette eller fleire", sammensatt)

indpros = []
tenpros = []

for x in over100:
    indpros.append((x[2], over100.index(x)))
    tenpros.append((x[3], over100.index(x)))

indpros.sort()
indpros.reverse()
tenpros.sort()
tenpros.reverse()

ind_antall = []
ind_næring = []
ten_antall = []
ten_næring = []

for i in range(0, 3):
    ind_antall.append(indpros[i][0])
    ind_næring.append(over100[indpros[i][1]][1])
    ten_antall.append(tenpros[i][0])
    ten_næring.append(over100[tenpros[i][1]][1])
    

plt.barh(ind_næring, ind_antall)
plt.title("Prosentandell av industriroboter i næringer med 100+ ansatte")
plt.grid(axis='x')
plt.show()
    
plt.barh(ten_næring, ten_antall)
plt.title("Prosentandell av tenesteroboter i næringer med 100+ ansatte")
plt.grid(axis='x')
plt.show()
