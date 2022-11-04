import pandas as pd
import pylab as py
from pylab import *
import statsmodels.api as sm
from scipy.optimize import curve_fit



#Leser inn data fra csv filen med pandas
tokyo = pd.read_csv('Middeltemperatur år - Tokyo.csv',sep=';')

#Lager lister med tidsdata og posisjonsdata
aar = tokyo['År']
temp = tokyo['Temp']



#Bestemmer k verdien og lager en tom liste for de nye verdiene
k = 7
temp_glatt = []

#Løkke som beregner de glattede temperaturene med glidende gjennomsnitt
for i in range(k,len(temp) - k):
    temp_glatt.append(py.mean(temp[(i - k):(i + k)]))



# Lowess = Locally Weighted Scatterplot Smoothing
lowess = sm.nonparametric.lowess    

#Beregner de glattede temperaturene med Lowess metoden
z = lowess(temp,aar,frac = 0.2,return_sorted = False)



aar_alt = []
for i in range(1,69,1):
    aar_alt.append(i)
    
x = linspace(0, 70, 1000)



#polyfit tar inn x og y verdier og siste parametere du oppgir tilpasser et n-te grads polynom
modell = polyfit(aar_alt, temp, 1)
#gir en array med koeffisientene i polynome, altså antall verdier i listen er n+1
#2 grads po
a_lin = modell[0]
b_lin = modell[1]



#Definerer den eksponentiale funksjonen
def fE(x, a, b):
    return a * b ** x

#Bestemmer a og b
[a_eks, b_eks] = curve_fit(fE, aar_alt, temp)[0]




#Definerer den logistiske funksjonen:
def fL(x, a, b, c):
  return c / (1 + a * exp(-b * x))

#Gir startverdier for parametrene:
a_s_log = 15.2
b_s_log = 0.24
c_s_log = 17.0

#Bestemmer og skriver ut a, b og c:
[a_log, b_log, c_log] = curve_fit(fL, aar_alt, temp, p0 = [a_s_log, b_s_log, c_s_log])[0]



# Lager lister med verdier for de ulike modellene
eks_verdier = []

for i in range(1, 69, 1):
    eks_verdier.append(fE(i, a_eks, b_eks))
    
z_verdier = []

for i in range(0, 68, 1):
    z_verdier.append(z[i])
    
lin_verdier = []

for i in range(1, 69, 1):
    lin_verdier.append(a_lin * i + b_lin)
    
log_verdier = []

for i in range(1, 69, 1):
    log_verdier.append(fL(i, a_log, b_log, c_log))
    
    
    
# Lager variabler til å holde verdiene til modellene
i = 0
    
dif_z = 0
dif_lin = 0
dif_eks = 0
dif_log = 0

tot_z = 0
tot_lin = 0
tot_eks = 0
tot_log = 0

tot_sum = []
 

   
# Løkke som beregner mest nøyaktige modell ved å se på forskjellen i avvik
while i < 68:
    tot_sum.clear()
    
    dif_eks = temp[i] - eks_verdier[i]
    if dif_eks < 0:
        dif_eks = dif_eks * -1
        tot_eks += dif_eks
        dif_eks = 0
    else:
        tot_eks += dif_eks
        dif_eks = 0

    dif_z = temp[i] - z_verdier[i]
    if dif_z < 0:
        dif_z = dif_z * -1
        tot_z += dif_z
        dif_z = 0
    else:
        tot_z += dif_z
        dif_z = 0

    dif_lin = temp[i] - lin_verdier[i]
    if dif_lin < 0:
        dif_lin = dif_lin * -1
        tot_lin += dif_lin
        dif_lin = 0
    else:
        tot_lin += dif_lin
        dif_lin = 0

    dif_log = temp[i] - log_verdier[i]
    if dif_log < 0:
        dif_log = dif_log * -1
        tot_log += dif_log
        dif_log = 0
    else:
        tot_log += dif_log
        dif_log = 0
    
    i += 1
    eks_liste = [tot_eks, 'eksponetiell regresjon']
    z_liste = [tot_z, 'lowess metoden']
    lin_liste = [tot_lin, 'linær regresjon']
    log_liste = [tot_log, 'logistisk regresjon']
    tot_sum.extend([eks_liste, z_liste, lin_liste, log_liste])
    tot_sum.sort()

print("Mest nøyaktige metode er", tot_sum[0][1])
    