import pandas as pd

file = pd.read_csv("roboter.csv", delimiter=';', encoding = "ISO-8859-1")

syssel = list(file["sysselsette"])
næring = list(file["næring"])
industri18 = list(file["Industrirobotar_2018"])
industri20 = list(file["Industrirobotar_2020"])
industri22 = list(file["Industrirobotar_2022"])

teneste18 = list(file["Tenesterobotar_2018"])
teneste20 = list(file["Tenesterobotar_2020"])
teneste22 = list(file["Tenesterobotar_2022"])