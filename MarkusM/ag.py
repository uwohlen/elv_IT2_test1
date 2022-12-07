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

