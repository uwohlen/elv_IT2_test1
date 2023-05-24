# importerer pandas, matplotlib og numpy
import pandas as pd, matplotlib.pyplot as plt, numpy as np

# leser inn data fra csv filen med pandas
datasett_import = pd.read_csv('googleplaystore.csv', sep=',')

# fjerner raden med indeks 10473, som er konfigurert feil i datasettet
datasett_import = datasett_import.drop([10473])

# fjerner alle radene med "nan" i datasettet ved bruk av pandas sin .dropna()
datasett = datasett_import.dropna()

# lager lister med data
apper = datasett["App"].tolist()
category = datasett["Category"].tolist()
rating = datasett["Rating"].tolist()
reviews = datasett["Reviews"].tolist() 
size = datasett["Size"].tolist()
installs = datasett["Installs"].tolist()
types = datasett["Type"].tolist()
price = datasett["Price"].tolist()
content_rating = datasett["Content Rating"].tolist()
genres = datasett["Genres"].tolist()
last_updated = datasett["Last Updated"].tolist()
current_ver = datasett["Current Ver"].tolist()
android_ver = datasett["Android Ver"].tolist()

# fjerner duplikater (beholder nyeste versjon)
'''
for i in range(0,len(apper)):
    for j in range(i+1,len(apper)):
        if j < len(apper) and apper[i] == apper[j]:
            if current_ver[i] > current_ver[j]:
                apper.pop(j), category.pop(j), rating.pop(j), reviews.pop(j), size.pop(j), installs.pop(j), types.pop(j), price.pop(j), content_rating.pop(j), genres.pop(j), last_updated.pop(j), current_ver.pop(j), android_ver.pop(j)
            else:
                apper.pop(i), category.pop(i), rating.pop(i), reviews.pop(i), size.pop(i), installs.pop(i), types.pop(i), price.pop(i), content_rating.pop(i), genres.pop(i), last_updated.pop(i), current_ver.pop(i), android_ver.pop(i)
'''
   
# lager ny liste med kategoriene
kategorier = []
for i in range(0,len(category)):
    if category[i] not in kategorier:
        kategorier.append(category[i])
        
# lager en ny liste med sjangerene
sjangere = []
for i in range(0,len(genres)):
    if genres[i] not in sjangere:
        sjangere.append(genres[i])

            
# lager en funksjon som finner antall apper i en kategori
def antall_funk(x):
    antall = 0
    for i in range(0,len(kategorier)):
        if kategorier[i] == x:
            antall += 1
    return antall

# lager en funksjon som finner antall apper i en sjanger
def antall_sjanger_funk(x):
    antall = 0
    for i in range(0,len(sjangere)):
        if sjangere[i] == x:
            antall += 1
    return antall

# lager en funksjon som finner antall apper i en kategori som er gratis
def antall_gratis_funk(x):
    antall = 0
    for i in range(0,len(category)):
        if category[i] == x and types[i] == 'Free':
            antall += 1
    return antall

# lager en funksjon som finner antall apper i en kategori som koster penger
def antall_betal_funk(x):
    antall = 0
    for i in range(0,len(category)):
        if category[i] == x and types[i] == 'Paid':
            antall += 1
    return antall

# lager en funksjon som finner antall apper i en kategori som er gratis og har en rating på y eller høyere
def antall_gratis_rating_funk(x, y):
    antall = 0
    for i in range(0,len(category)):
        if category[i] == x and types[i] == 'Free' and rating[i] >= y:
            antall += 1
    return antall

# lager en funksjon som finner antall apper i en kategori som koster penger og har en rating på y eller høyere
def antall_betal_rating_funk(x, y):
    antall = 0
    for i in range(0,len(category)):
        if category[i] == x and types[i] == 'Paid' and rating[i] >= y:
            antall += 1
    return antall
        
# lager en funksjon som sorterer en kategori etter antall nedlastninger (fjerner "+" fra tallene og konverterer til int)
def nedlastninger_sortert_funk(x):
    nedlastninger_sortert = []
    apper_sortert = []
    for i in range(0,len(category)):
        if category[i] == x:
            nedlastninger_sortert.append(int(installs[i].replace("+","").replace(",","")))
            apper_sortert.append(apper[i])
    nedlastninger_sortert, apper_sortert = zip(*sorted(zip(nedlastninger_sortert, apper_sortert)))
    nedlastninger_sortert, apper_sortert = (list(t) for t in zip(*sorted(zip(nedlastninger_sortert, apper_sortert))))
    return nedlastninger_sortert, apper_sortert

# lager en funksjon som sorterer apper etter sist oppdatert (tar bare med årstall og konverterer til int)
def oppdatert_sortert_funk(x):
    oppdatert_sortert = []
    apper_sortert = []
    for i in range(0,len(category)):
        if category[i] == x:
            oppdatert_sortert.append(int(last_updated[i][-4:]))
            apper_sortert.append(apper[i])
    oppdatert_sortert, apper_sortert = zip(*sorted(zip(oppdatert_sortert, apper_sortert)))
    oppdatert_sortert, apper_sortert = (list(t) for t in zip(*sorted(zip(oppdatert_sortert, apper_sortert))))
    return oppdatert_sortert, apper_sortert

# lager en funksjon som sorter alle appene i en kategori etter rating med navn og ekskluderer alle appene med "nan" som rating
def rating_sortert_funk(x):
    rating_sortert = []
    apper_sortert = []
    for i in range(0,len(category)):
        if category[i] == x:
            rating_sortert.append(rating[i])
            apper_sortert.append(apper[i])
    rating_sortert, apper_sortert = zip(*sorted(zip(rating_sortert, apper_sortert)))
    rating_sortert, apper_sortert = (list(t) for t in zip(*sorted(zip(rating_sortert, apper_sortert))))
    return rating_sortert, apper_sortert

'''
# lager et kakediagramm som viser appene i kategorien "ART_AND_DESIGN" etter nedlastninger
plt.subplot(2, 1, 1)
nedlastninger_sortert, apper_sortert = nedlastninger_sortert_funk("ART_AND_DESIGN")
plt.pie(nedlastninger_sortert, labels=apper_sortert, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Nedlastninger i kategorien 'ART_AND_DESIGN'")
plt.axis('equal')
plt.show()
'''

'''
# lager et søylediagramm som viser topp 10 appene i kategorien "ART_AND_DESIGN" etter nedlastninger
plt.subplot(2, 1, 2)
nedlastninger_sortert, apper_sortert = nedlastninger_sortert_funk("ART_AND_DESIGN")
nedlastninger_sortert = nedlastninger_sortert[len(nedlastninger_sortert)-11:len(nedlastninger_sortert)]
apper_sortert = apper_sortert[len(apper_sortert)-11:len(apper_sortert)]
plt.barh(apper_sortert, nedlastninger_sortert)
plt.title("Topp 10 nedlastninger i kategorien 'ART_AND_DESIGN'")
plt.xlabel("Nedlastninger i millioner")
plt.ylabel("App")
plt.grid()
plt.show()
'''

'''
# lager et kakediagram som viser antall apper i hver kategori
antall = []
for i in range(0,len(kategorier)):
    antall.append(antall_funk(kategorier[i]))
plt.pie(antall[-11:], labels=kategorier[-11:], autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p, p * sum(antall[-11:])/100), shadow=False, startangle=90, rotatelabels=False, labeldistance=1.1, textprops={'fontsize': 8})
plt.title("Antall apper i hver kategori")
plt.axis('equal')
plt.show()
'''

'''
# lager et søylediagramm som viser antall apper i hver kategori
antall = []
for i in range(0,len(kategorier)):
    antall.append(antall_funk(kategorier[i]))
plt.barh(kategorier[-11:], antall[-11:])
plt.title("Antall apper i hver kategori")
plt.xlabel("Antall apper")
plt.ylabel("Kategori")
plt.grid()
plt.show()
'''

'''
# lager et kakediagram som viser antall apper i hver sjanger
antall = []
for i in range(0,len(sjangere)):
    antall.append(antall_funk(sjangere[i]))
plt.pie(antall[-11:], labels=sjangere[-11:], autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p, p * sum(antall[-11:])/100), shadow=False, startangle=90, rotatelabels=False, labeldistance=1.1, textprops={'fontsize': 8})
plt.title("Antall apper i hver sjanger")
plt.axis('equal')
plt.show()
'''

'''
# lager et histogram som viser apper etter hvor mye de koster i kategorien "ART_AND_DESIGN"
pris = []
for i in range(0,len(category)):
    if category[i] == "ART_AND_DESIGN":
        pris.append(float(price[i]))
plt.hist(pris, bins=100)
plt.title("Pris på apper i kategorien 'ART_AND_DESIGN'")
plt.xlabel("Pris i dollar")
plt.ylabel("Antall apper")
plt.grid()
plt.show()
'''

'''
# lager et punktdiagram som viser apper etter hvor mye de koster i kategorien "ART_AND_DESIGN"
pris = []
for i in range(0,len(category)):
    if category[i] == "ART_AND_DESIGN":
        pris.append(float(price[i]))
plt.plot(apper, pris, 'o')
plt.title("Pris på apper i kategorien 'ART_AND_DESIGN'")
plt.xlabel("App")
plt.ylabel("Pris i dollar")
plt.grid()
plt.show()
'''

'''
# lager et linjeplott som viser apper etter hvor mye de koster i kategorien "ART_AND_DESIGN"
pris = []
for i in range(0,len(category)):
    if category[i] == "ART_AND_DESIGN":
        pris.append(float(price[i]))
plt.plot(apper, pris)
plt.title("Pris på apper i kategorien 'ART_AND_DESIGN'")
plt.xlabel("App")
plt.ylabel("Pris i dollar")
plt.grid()
plt.show()
'''