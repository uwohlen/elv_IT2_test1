rekkefolge = "abcdefghijklmnopqrstuvwxyzæøå"

def navn_verdi(navn):
    total_verdi = 0
    i = 1
    maks = len(rekkefolge) * 2
    for bokstav in navn:
        indeks = rekkefolge.index(bokstav.lower())
        verdi = indeks * 2 + (1 if bokstav.islower() else 0)
        total_verdi += verdi / (maks**i)
        i += 1
    return total_verdi

def sorter_navn(navn):
    navn.sort(key=navn_verdi)

navn = ["Alexander", "Azeem", "Benjamin", "Birk", "Elias", "MarkusJ", "MarkusM", "Simen", "Unni", "bæærdia", "danial", "jarand", "jennica", "sondre", "Øystein"]
sorter_navn(navn)
print(navn)