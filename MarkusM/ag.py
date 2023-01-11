import math

a = 0 #nedre grense
b = 20 #øvre grense
n = 10 #antall trapeser

def f(x): #funksjonen som skal integreres numerisk
    return 5*(math.sin(0.1*x))

deltax = (b-a)/n #trapesbredden

s = 0 #sum

for i in range(1,n): #fra 1 til n-1
    s += f(a+i*deltax) #summen av trapesene
s = (deltax/2)*(2*s+f(a)+f(b)) #tar delax/2(f(a)+f(b)+trapessummen)

print(round(s,3)) #printer svaret

print(math.degrees((5*math.pi)/12))



     














"""
import sys
dødelig = False
inntak = 50 #mg
total = 0 #totalt
nedbrytningsgrad = 0.68
i = 0 #dag nr

while not dødelig:
    total = total*nedbrytningsgrad #skjer over et døgn, så må skje først i løkken

    i +=1 #inkrimentere teller
    total += inntak #legge til daglig inntak

    if total > 130: #hvis det blir dødelig
        dødelig = True

    if i > 100: #hvis det ikke vlir dødelig
        print("Medisininntaket ble ikke dødelig, siden den ikke nådde mer enn 130 mg av virkestoffet i kroppen samtidig")
        print(f"Den høyeste verdien ble {total} mg")
        sys.exit()


print(f"medisinen ble dødelig etter {i} dager, siden {total} mg av virkestoffet var i kroppen samtidig")

"""
"""
s = 0

for i in range(12):
    s+= ((i)*3)+2
    print(s)
print(s)
#print(37*12)
"""

"""
s = 0 #sum
a = 0 #nedre grense
b = 2 #øvre grense
n = 1000 #nøtaktighet

def f(x):
    return x**2

deltax = (b-a)/n


for i in range(n):
    s+= f(a+(i*deltax))*deltax

print(s)
"""

