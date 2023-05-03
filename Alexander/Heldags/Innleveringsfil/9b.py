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
    sammensatt.append((syssel[x], næring[x], industri20[x]))
    
def hent(index, value, lst):
    ret = []
    for i in range(len(lst)):
        if lst[i][index] == value:
            ret.append(lst[i])
            
    return ret


industri = hent(1, "10-39 Industri, kraftforsyning, vatn, avløp og renovasjon", sammensatt)
agentur = hent(1, "46 Agentur- og engroshandel med unntak av motorvogner", sammensatt)
informasjon = hent(1, "58-63 Informasjon og kommunikasjon", sammensatt)

industri.remove(industri[0])
agentur.remove(agentur[0])
informasjon.remove(informasjon[0])

alle = [industri, agentur, informasjon]
for verdi in alle:
    pros = []
    navn = []
    for x in range(len(verdi)):
        navn.append(verdi[x][0][:5])
        pros.append(verdi[x][2])
        
    plt.bar(navn, pros)
    plt.title(f"Prosentandell av industriroboter i {verdi[0][1]}")
    plt.xlabel("ansatte")
    plt.grid(axis='y')
    plt.show()




