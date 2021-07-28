#Módulo de Daziel
# Importe el módulo dalziel y ejecute la función avgcity con una sola ciudad
input("ciudad: ")
import pandas as pd
df=pd.read_csv("Dalziel2016_data.csv")
casos= df["cases"][0:1118]
sumacasos= df["cases"][0:1118].sum()
poblacion=df["pop"][0:1118].sum()
print("Casos de BALTIMORE", "=", sumacasos)
print("Poblacion de BALTIMORE", "=", poblacion)
avgcity = sumacasos/poblacion
print("Promedio(casos/poblacion)BALTIMORE ", "=", avgcity)
# Importe el módulo dalziel y ejecute la función avgcity con un listados de ciudades
input("ciudad1: ")
input("ciudad2: ")
input("ciudad3: ")
import pandas as pd
df=pd.read_csv("Dalziel2016_data.csv")
BALTIMOREcasos= df["cases"][0:1118].sum()
BOSTONcasos= df["cases"][1119:2236].sum()
BRIDGEPORTcasos= df["cases"][2237:3354].sum()
BALTIMOREpoblacion=df["pop"][0:1118].sum()
BOSTONpoblacion=df["pop"][1119:2236].sum()
BRIDGEPORTpoblacion=df["pop"][2237:3354].sum()
BALTIMOREavgcity = BALTIMOREcasos/BALTIMOREpoblacion
a= print("BALTIMORE", "=",BALTIMOREavgcity)
BOSTONavgcity = BOSTONcasos/BOSTONpoblacion
b= print("BOSTON", "=",BOSTONavgcity)
BRIDGEPORTavgcity = BRIDGEPORTcasos/BRIDGEPORTpoblacion
c=print("BRIDGEPORT", "=", BRIDGEPORTavgcity)
