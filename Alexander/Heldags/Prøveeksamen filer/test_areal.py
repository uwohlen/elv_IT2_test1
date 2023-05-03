def areal(lengde,bredde):
    try:
        tmp = int(lengde) # passer på lendge og bredde er tall
        tmp = int(bredde)
        if lengde < 0 or bredde < 0: # passer på lengde og bredde er større eller lik 0
            return "Ikke et areal"
        else:
            return lengde*bredde
    except:
        return "Ikke et areal"

def test_areal():
    verdier_inn = [-1000000000,-1,0,0.5,1,10,1000000000]

    arealer_forventet = ["Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal","Ikke et areal",0,0.0,0,0,0,"Ikke et areal","Ikke et areal",0.0,0.25,0.5,5.0,500000000.0,"Ikke et areal","Ikke et areal",0,0.5,1,10,1000000000,"Ikke et areal","Ikke et areal",0,5.0,10,100,10000000000,"Ikke et areal","Ikke et areal",0,500000000.0,1000000000,10000000000,1000000000000000000]

    i = 0
    for lengde in verdier_inn:
        for bredde in verdier_inn:
            test = areal(lengde,bredde)
            kontroll = arealer_forventet[i]
            if test == kontroll:
                print("Funksjonen virker")
            else:
                print(f"Funksjonen areal {test:25.2f} virker ikke for lengden {lengde:15.1f} og bredden {bredde:15.1f}")
            i += 1

test_areal()