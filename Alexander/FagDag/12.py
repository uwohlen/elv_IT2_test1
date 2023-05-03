import pandas as pd
from matplotlib import pyplot as plt

file = pd.read_csv("11419_20230324-122526.csv", skiprows=2, delimiter=";", encoding = "ISO-8859-1")

år15 = list(file["Månedslønn (kr) 2015"])
år22 = list(file["Månedslønn (kr) 2022"])
yrke = list(file["yrke"])
næring = list(file["næring (SN2007)"])
kjønn = list(file["kjønn"])

print(max(år22))
pros = []
for i in range(len(år15)):
    try:
        pros.append(((int(år22[i]) / int(år15[i])) - 1, i))
    except:
        pros.append(None)
        
def sort_func(n):
    try:
        return n[0]
    except:
        return -100

pros.sort(key = sort_func)

for x in range(pros.count(None)):
    pros.pop(0)
    
x = []
y1 = []
y2 = []
for i in range(1, 4):
    x.append(f"{yrke[pros[-i][1]]}, {næring[pros[-i][1]]}, {kjønn[pros[-i][1]]}")
    y1.append(round(pros[-i][0] * 100, 2))
    y2.append(round(pros[i - 1][0] * 100,2))
    
plt.barh(x, y1)
plt.xlim(50, 55)
plt.title("Kombinasjon av yrke, næring og kjønnn som har hatt størst lønnsøkning mellom 2015 og 2022")
plt.xlabel("Prosent Lønn Økning")
plt.ylabel("Yrke, Næring, Kjønn")
plt.show()
plt.barh(x, y2)
plt.xlim(-20, 0)
plt.title("Kombinasjon av yrke, næring og kjønnn som har hatt minst lønnsøkning mellom 2015 og 2022")
plt.xlabel("Prosent Lønn Økning")
plt.ylabel("Yrke, Næring, Kjønn")
plt.show()

ledere = []
admin = []
akad = []
høy = []
kont = []
salg = []
bønd = []
hånd = []
pross = []
ren = []

for x in file.index:
        #if file.loc[x, "Månedslønn (kr) 2015"] == ':' or file.loc[x, "Månedslønn (kr) 2016"] == ':' or file.loc[x, "Månedslønn (kr) 2017"] == ':' or file.loc[x, "Månedslønn (kr) 2018"] == ':' or file.loc[x, "Månedslønn (kr) 2019"] == ':' or file.loc[x, "Månedslønn (kr) 2020"] == ':' or file.loc[x, "Månedslønn (kr) 2021"] == ':' or file.loc[x, "Månedslønn (kr) 2022"] == ':':
    if file.loc[x, "yrke"] == "Ledere":
        ledere.append(x)
    if file.loc[x, "yrke"] == "Administrerende direktører":
        admin.append(x)
    if file.loc[x, "yrke"] == "Akademiske yrker":
        akad.append(x)
    if file.loc[x, "yrke"] == "Høyskoleyrker":
        høy.append(x)
    if file.loc[x, "yrke"] == "Kontoryrker":
        kont.append(x)
    if file.loc[x, "yrke"] == "Salgs- og serviceyrker":
        salg.append(x)
    if file.loc[x, "yrke"] == "Bønder, fiskere mv.":
        bønd.append(x)
    if file.loc[x, "yrke"] == "Håndverkere":
        hånd.append(x)
    if file.loc[x, "yrke"] == "Prosess- og maskinoperatører, transportarbeidere mv.":
        pross.append(x)
    if file.loc[x, "yrke"] == "Renholdere, hjelpearbeidere mv.":
        ren.append(x)

def gj(lst, år, kjønn): #kjønn 0 for mann 1 for dame
    summ = 0
    count = 0
    for x in range(kjønn, len(lst), 2):
        try:
            summ += int(file[f"Månedslønn (kr) {år}"][lst[x]])
            count += 1
        except:
            continue
    return summ / count

def mmap(lst, står, slår, kjønn):
    ret = []
    for x in range(står, slår + 1):
        ret.append(gj(lst, x, kjønn))
    return ret

x = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022] 
mledere = mmap(ledere, 2015, 2022, 0)
madmin = mmap(admin, 2015, 2022, 0)
makad = mmap(akad, 2015, 2022, 0)
mhøy = mmap(høy, 2015, 2022, 0)
mkont = mmap(kont, 2015, 2022, 0)
msalg = mmap(salg, 2015, 2022, 0)
mbønd = mmap(bønd, 2015, 2022, 0)
mhånd = mmap(hånd, 2015, 2022, 0)
mpross = mmap(pross, 2015, 2022, 0)
mren = mmap(ren, 2015, 2022, 0)

plt.plot(x, mledere, label="ledere")
plt.plot(x, madmin, label="Administrerende direktører")
plt.plot(x, makad, label="Akademiske yrker")
plt.plot(x, mhøy, label="Høyskoleyrker")
plt.plot(x, mkont, label="Kontoryrker")
plt.plot(x, msalg, label="Salgs- og serviceyrker")
plt.plot(x, mbønd, label="Bønder, fiskere mv.")
plt.plot(x, mhånd, label="Håndverkere")
plt.plot(x, mpross, label="Prosess- og maskinoperatører, transportarbeidere mv.")
plt.plot(x, mren, label="Renholdere, hjelpearbeidere mv.")
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.title("Månedes lønn for menn i forskjellige yrker")
plt.ylabel("Kroner")
plt.xlabel("År")
plt.show()

x = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022] 
mledere = mmap(ledere, 2015, 2022, 1)
madmin = mmap(admin, 2015, 2022, 1)
makad = mmap(akad, 2015, 2022, 1)
mhøy = mmap(høy, 2015, 2022, 1)
mkont = mmap(kont, 2015, 2022, 1)
msalg = mmap(salg, 2015, 2022, 1)
mbønd = mmap(bønd, 2015, 2022, 1)
mhånd = mmap(hånd, 2015, 2022, 1)
mpross = mmap(pross, 2015, 2022, 1)
mren = mmap(ren, 2015, 2022, 1)

plt.plot(x, mledere, label="ledere")
plt.plot(x, madmin, label="Administrerende direktører")
plt.plot(x, makad, label="Akademiske yrker")
plt.plot(x, mhøy, label="Høyskoleyrker")
plt.plot(x, mkont, label="Kontoryrker")
plt.plot(x, msalg, label="Salgs- og serviceyrker")
plt.plot(x, mbønd, label="Bønder, fiskere mv.")
plt.plot(x, mhånd, label="Håndverkere")
plt.plot(x, mpross, label="Prosess- og maskinoperatører, transportarbeidere mv.")
plt.plot(x, mren, label="Renholdere, hjelpearbeidere mv.")
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.title("Månedes lønn for kvinner i forskjellige yrker")
plt.ylabel("Kroner")
plt.xlabel("År")
plt.show()
