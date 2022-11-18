class Person:
    """Klasse for å lagre personopplysninger

    Parametre:
        fornavn (str): Personens fornavn og eventuelle mellomnavn
        etternavn (str): Personens etternavn
        fodselsar (int): Personens fødselsår med 4 siffer
    """
    def __init__(self, fornavn:str, etternavn:str, fodselsar:int):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fodselsar = fodselsar

unni = Person("Unni", "Wohlen", 1970)