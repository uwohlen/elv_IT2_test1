import random

batteri = random.randint(1,100)

halv = 50

lavt = 10

print("Batteri nivået er", batteri)

if batteri  < halv and batteri > lavt:
    print("Batteriet er middels fullt")
    
elif batteri < lavt:
    print("Batteriet er lavt")

else:
    print("Batteriet er høyt")

print("Hei")
print("nei")
