

navn=input("Hva heter du? ") #bruker input og output
print("Hei " + navn + "!")
alder=input("Hvor gammel er du? ")
alder=int(alder) #bruker integer for å gjøre tekstdatatypen til heltalldatatype

def sjekkMyndig(alder): #funksjon som skal sjekke om personen er myndig gjennom tester
    if alder > 17:
        print("Du er myndig!!")
    elif 16 < alder < 18:
        print("Du er veldig snart myndig!!")
    else:
        print("Du er ikke myndig")

jennicaAlder = 18 #variabel
if jennicaAlder > alder:
    diff = jennicaAlder - alder
    print("Du er", diff, "år yngre enn Jennica")
elif jennicaAlder == alder:
    print("Du er like gammel som Jennica")
else:
    diff = alder - jennicaAlder
    print("Du er", diff, "år eldre enn Jennica")


ord_liste = ["takk", "for", "at", "du", "bruker", "jennicas", "program"] #lister og for-løkke som stoppes før den har gått gjennom hele lista
for navn in ord_liste:
    print(navn)
    if navn == "jennicas":
        break
print("the end")

#i = 1
#while i < 5:
#    print(i)
 
#While løkken vil være uendelig fordi utsagnet alltid vil være sant og kræsje programmet