print("Skriv inn et regnestykke: ")
while True:
    user_input = input()

    har_sett_tegn = False
    tall1_float = False
    tall2_float = False
    tegn_posisjon = 0
    minus = False
    ugyldig = False
    for i, bokstav in enumerate(user_input):
        if bokstav == ".":
            if har_sett_tegn:
                if tall2_float == True:
                    ugyldig = True
                    print("Tall 2 kan ikke inneholde flere punktum")
                    break
                tall2_float = True
            else:
                if tall1_float == True:
                    ugyldig = True
                    print("Tall 1 kan ikke inneholde flere punktum")
                    break
                tall1_float = True
            continue
        if bokstav == "-" or bokstav == "+":
            if har_sett_tegn:
                ugyldig = True
                print("Det kan kun være én regneoperator")
                break
            har_sett_tegn = True
            tegn_posisjon = i
            if tegn_posisjon == 0:
                ugyldig = True
                print("Det må være et tall før regneoperatoren")
            if tegn_posisjon == len(user_input)-1:
                ugyldig = True
                print("Det må være et tall etter regneoperatoren")
            minus = True if bokstav == "-" else False
            continue
        if not bokstav in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            ugyldig = True
            print(f"Regnestykket inneholdt ugyldig karakter: {bokstav}")
            break

    if ugyldig == False and har_sett_tegn == False:
        ugyldig = True
        print("Regnestykket må inneholde en regneoperator")

    if ugyldig:
        print("Skriv inn på nytt:")
        continue

    tall1 = 0
    if tall1_float:
        tall1 = float(user_input[:tegn_posisjon])
    else:
        tall1 = int(user_input[:tegn_posisjon])

    tall2 = 0
    if tall2_float:
        tall2 = float(user_input[tegn_posisjon+1:])
    else:
        tall2 = int(user_input[tegn_posisjon+1:])

    resultat = 0
    if minus:
        resultat = tall1 - tall2
    else:
        resultat = tall1 + tall2
    print(f"Resultatet er: {resultat}")
    break