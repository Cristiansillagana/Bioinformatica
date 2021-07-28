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
# Importe el módulo dalziel y ejecute la función avgyear con el valor predeterminado de ciudad
input("ciudad:")
import pandas as pd
df=pd.read_csv("Dalziel2016_data.csv")
AÑOS=df["year"][0:1118]
CASOS=df["cases"][0:1118]
POBLACION=df["pop"][0:1118]
#ahora para un determinado año
años=df["year"][0:26]
casos=df["cases"][0:26].sum()
poblacion=df["pop"][0:26].sum()
avgyear= casos/poblacion
print("BALTIMORE", "1906", avgyear)
# Importe el módulo dalziel y ejecute la función avgyear con un listado de ciudades
input("ciudad1: ")
input("ciudad2: ")
input("ciudad3: ")
import pandas as pd
df=pd.read_csv("Dalziel2016_data.csv")
#ahora para un determinado año
#BALTIMORE
años=df["year"][0:26]
BALcasos=df["cases"][0:26].sum()
BALpoblacion=df["pop"][0:26].sum()
BALavgyear= casos/poblacion
#BOSTON
BOScasos=df["cases"][1119:1145].sum()
BOSpoblacion=df["pop"][1119:1145].sum()
BOSavgyear= casos/poblacion
#BRIDGEPORT
BRIGcasos=df["cases"][2237:2262].sum()
BRIGpoblacion=df["pop"][2237:2262].sum()
BALavgyear= casos/poblacion
print("BALTIMORE", "1906", avgyear)
print("BOSTON", "1906", avgyear)
print("BRIDGEPORT", "1906", avgyear)
# Importe el módulo dalziel y ejecute la función avgyear con un listado de años
#input("ciudad1: ")
#input("ciudad2: ")
#input("ciudad3: ")
import pandas as pd
df=pd.read_csv("Dalziel2016_data.csv")
#ahora para un determinado año
#BALTIMORE
#1906
BALcasos11=df["cases"][0:26].sum()
BALpoblacion11=df["pop"][0:26].sum()
avgyear11= BALcasos11/BALpoblacion11
#1910
BALcasos21=df["cases"][105:130].sum()
BALpoblacion21=df["pop"][105:130].sum()
avgyear21= BALcasos21/BALpoblacion21
#1925
BALcasos31=df["cases"][495:520].sum()
BALpoblacion31=df["pop"][495:520].sum()
avgyear31= BALcasos31/BALpoblacion31
#BOSTON
#1906
BOScasos12=df["cases"][1119:1145].sum()
BOSpoblacion12=df["pop"][1119:1145].sum()
avgyear12= BOScasos12/BOSpoblacion12
#1910
BOScasos22=df["cases"][1223:1248].sum()
BOSpoblacion22=df["pop"][1223:1248].sum()
avgyear22= BOScasos22/BOSpoblacion22
#1925
BOScasos32=df["cases"][1614:1637].sum()
BOSpoblacion32=df["pop"][1614:1637].sum()
avgyear32= BOScasos32/BOSpoblacion32
#BRIDGEPORT
#1906
BRIGcasos13=df["cases"][2237:2262].sum()
BRIGpoblacion13=df["pop"][2237:2262].sum()
avgyear13= BRIGcasos13/BRIGpoblacion13
#1910
BRIGcasos23=df["cases"][2341:2366].sum()
BRIGpoblacion23=df["pop"][2341:2366].sum()
avgyear23= BRIGcasos23/BRIGpoblacion23
#1925
BRIGcasos33=df["cases"][2731:2756].sum()
BRIGpoblacion33=df["pop"][2731:2756].sum()
avgyear33= BRIGcasos33/BRIGpoblacion33

A={
    "BALTIMORE":["1906",avgyear11],
    "BALTIMORE":["1910",avgyear21],
    "BATIMORE":["1925",avgyear31],
    "BOSTON":["1906",avgyear12],
    "BOSTON":["1910",avgyear22],
    "BOSTON":["1925",avgyear32],
    "BRIDGEPORT":["1906",avgyear13],
    "BRIDGEPORT":["1910",avgyear23],
    "BRIDGEPORT":["1925",avgyear23],
}
print(A)
# Importe el módulo dalziel y ejecute la función avgyear con un listado de años
#input("ciudad1: ")
#input("ciudad2: ")
#input("ciudad3: ")
import pandas as pd
df=pd.read_csv("Dalziel2016_data.csv")
#ahora para un determinado año
#BALTIMORE
#1906
BALcasos11=df["cases"][0:26].sum()
BALpoblacion11=df["pop"][0:26].sum()
avgyear11= BALcasos11/BALpoblacion11
#1910
BALcasos21=df["cases"][105:130].sum()
BALpoblacion21=df["pop"][105:130].sum()
avgyear21= BALcasos21/BALpoblacion21
#1925
BALcasos31=df["cases"][495:520].sum()
BALpoblacion31=df["pop"][495:520].sum()
avgyear31= BALcasos31/BALpoblacion31
#BOSTON
#1906
BOScasos12=df["cases"][1119:1145].sum()
BOSpoblacion12=df["pop"][1119:1145].sum()
avgyear12= BOScasos12/BOSpoblacion12
#1910
BOScasos22=df["cases"][1223:1248].sum()
BOSpoblacion22=df["pop"][1223:1248].sum()
avgyear22= BOScasos22/BOSpoblacion22
#1925
BOScasos32=df["cases"][1614:1637].sum()
BOSpoblacion32=df["pop"][1614:1637].sum()
avgyear32= BOScasos32/BOSpoblacion32
#BRIDGEPORT
#1906
BRIGcasos13=df["cases"][2237:2262].sum()
BRIGpoblacion13=df["pop"][2237:2262].sum()
avgyear13= BRIGcasos13/BRIGpoblacion13
#1910
BRIGcasos23=df["cases"][2341:2366].sum()
BRIGpoblacion23=df["pop"][2341:2366].sum()
avgyear23= BRIGcasos23/BRIGpoblacion23
#1925
BRIGcasos33=df["cases"][2731:2756].sum()
BRIGpoblacion33=df["pop"][2731:2756].sum()
avgyear33= BRIGcasos33/BRIGpoblacion33

print({
    "BALTIMORE":[1906,avgyear11],
    "BOSTON":[1906,avgyear12],
    "BRIDGEPORT":[1906,avgyear13]
})
print({
    "BALTIMORE":[1910,avgyear21],
    "BOSTON":[1910,avgyear22],
    "BRIDGEPORT":[1910,avgyear23]
})
print({    
     "BALTIMORE":[1925,avgyear31],
    "BOSTON":[1925,avgyear32],
    "BRIDGEPORT":[1925,avgyear23]
})
