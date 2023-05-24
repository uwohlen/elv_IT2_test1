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

# finner næringene med 100 eller flere sysselsatte og legger dem inn i en liste
def næring_funk(x):
    ansatte_100_næringer = []
    for i in range(0,len(x)):
        if x[i] == "100 sysselsette eller fleire":
            ansatte_100_næringer.append(næring[i])
    return ansatte_100_næringer

# finner antall industriroboter i 2022 får næringene med 100 eller flere sysselsatte
def roboter_funk(x, y):
    roboter = []
    for i in range(0,len(x)):
        if x[i] == "100 sysselsette eller fleire":
            roboter.append(y[i])
    return roboter

# sorterer listene i stigende rekkefølge med tilsvarende næring og antall roboter med samme indeks
# for industriroboter 2022
roboter_sortert, næring_sortert = zip(*sorted(zip(roboter_funk(sysselsatte, industri_2022), næring_funk(sysselsatte))))
roboter_sortert, næring_sortert = (list(t) for t in zip(*sorted(zip(roboter_funk(sysselsatte, industri_2022), næring_funk(sysselsatte)))))

print("De tre næringene med 100 eller flere ansatte som har flest industriroboter i 2022 er", næring_sortert[len(næring_sortert)-1],"og", næring_sortert[len(næring_sortert)-2],"og", næring_sortert[len(næring_sortert)-3])

# lager liste for industriroboter
top3næring = [næring_sortert[len(næring_sortert)-1], næring_sortert[len(næring_sortert)-2], næring_sortert[len(næring_sortert)-3]]
top3tall = [roboter_sortert[len(roboter_sortert)-1], roboter_sortert[len(roboter_sortert)-2], roboter_sortert[len(roboter_sortert)-3]]

# plot for industriroboter
plt.subplot(2, 1, 1)
plt.bar(top3næring, top3tall)
plt.xlabel("Næringer med 100 eller flere ansatte")
plt.ylabel("Prosent andel av industriroboter i 2022")
plt.grid()



# sorterer listene i stigende rekkefølge med tilsvarende næring og antall roboter med samme indeks
# for tjenesteroboter 2022
roboter_sortert, næring_sortert = zip(*sorted(zip(roboter_funk(sysselsatte, tjeneste_2022), næring_funk(sysselsatte))))
roboter_sortert, næring_sortert = (list(t) for t in zip(*sorted(zip(roboter_funk(sysselsatte, tjeneste_2022), næring_funk(sysselsatte)))))

print("De tre næringene med 100 eller flere ansatte som har flest tjenesteroboter i 2022 er", næring_sortert[len(næring_sortert)-1],"og", næring_sortert[len(næring_sortert)-2],"og", næring_sortert[len(næring_sortert)-3])

# lager liste for tjenesteroboter
top3næring = [næring_sortert[len(næring_sortert)-1], næring_sortert[len(næring_sortert)-2], næring_sortert[len(næring_sortert)-3]]
top3tall = [roboter_sortert[len(roboter_sortert)-1], roboter_sortert[len(roboter_sortert)-2], roboter_sortert[len(roboter_sortert)-3]]

# plot for tjenesteroboter
plt.subplot(2, 1, 2)
plt.bar(top3næring, top3tall)
plt.xlabel("Næringer med 100 eller flere ansatte")
plt.ylabel("Prosent andel av tjenesteroboter i 2022")
plt.grid()
plt.show()
