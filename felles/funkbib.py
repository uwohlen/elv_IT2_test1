def leggSammenListe(liste: list):
    """Summerer elementene i en liste. 
    En input, av typen liste, elementene må være av samme type. 
    En output, type returnert er avhengig av type elementer i input.
    UW"""
    summen = liste[0]
    for i in range(1,len(liste)):
        summen += liste[i]
    return summen
