import pandas as pd
from pylab import *
import matplotlib.pyplot as plt

#Leser inn data fra csv filen med pandas
datasett = pd.read_csv('roboter.csv', sep=';')

#Lager lister med data
sysselsatte = datasett["sysselsette"]
næring = datasett["næring"]
industri_2018 = datasett["Industrirobotar_2018"]
industri_2020 = datasett["Industrirobotar_2020"]
industri_2022 = datasett["Industrirobotar_2022"]
tjeneste_2018 = datasett["Tenesterobotar_2018"]
tjeneste_2020 = datasett["Tenesterobotar_2020"]
tjeneste_2022 = datasett["Tenesterobotar_2022"]

# finner antall roboter til en næring
def næring_funk(x, y, z):
    næringer = []
    i = 1
    for i in range(0,len(x)):
        if x[i] != "Alle sysselsette" and næring[i] == y:
            næringer.append(z[i])
    return næringer

# bruker næring_funk for å lage liste med antall roboter
næring10_39 = næring_funk(sysselsatte, "10-39 Industri, kraftforsyning, vatn, avløp og renovasjon", industri_2020)
næring46 = næring_funk(sysselsatte, "46 Agentur- og engroshandel med unntak av motorvogner", industri_2020)
næring58_63 = næring_funk(sysselsatte, "58-63 Informasjon og kommunikasjon", tjeneste_2020)

# lager liste med størrelse på bedriftene
størrelse = ["10-19 sysselsatte", "20-49 sysselsatte", "50-99 sysselsatte", "100 eller flere sysselsatte"]

# lager graf med alle bedriftene og antall roboter
plt.plot(størrelse, næring10_39, color="navy", marker="D", label="10-39 Industri, kraftforsyning, vatn, avløp og renovasjon")
plt.plot(størrelse, næring46, color="darkred", marker="D", label="46 Agentur- og engroshandel med unntak av motorvogner")
plt.plot(størrelse, næring58_63, color="olive", marker="D", label="58-63 Informasjon og kommunikasjon")
plt.xlabel("Antall sysselsatte")
plt.ylabel("Prosent andel roboter i 2020")
plt.legend()
plt.grid()
plt.show()
