personer = []
person = input("Skriv inn navn, alder og kjoenn (mann, kvinner eller annet) med komma mellom: ")

def leggtilperson(person):
    navneliste = person.split(",")
    navn=[verdi.strip(" ") for verdi in navneliste] #fjerner eventuelle mellomrom fra input
    liste={"navn": navn[0].capitalize(), "alder":int(navn[1]),"kjoenn":navn[2].capitalize()}
    personer.append(liste)
    
leggtilperson(person)

menn=[]
kvinner=[]
annet=[]

for i in personer:
    if i['alder']<18:
        print('Du er ikke gammel nok! Du må være 18 år')
        personer.remove(i)
    if i['kjoenn']=="Mann":
        menn+= i.items()
    elif i["kjoenn"]=="kvinne":
        kvinner+=i.items()
    else:
        annet+=i.items()
        
print("hei")