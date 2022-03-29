añoInicial=1500
añoFinal=2022
r="Loas años bisienstos entre "+str(añoInicial )+" Y "+str(añoFinal)+" Son: "
for i in range (añoInicial,añoFinal):
   if i%4==0 and i%400==0:
        r+=r+str(i)+","

print(r)
