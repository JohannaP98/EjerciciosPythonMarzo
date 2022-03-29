correctos = int (input("Ingrese el número de aciertos: "))
errores = int (input("Ingrese el número de errores: "))
total = correctos + errores
pCorrectos = (100/total)*correctos
pErrores = (100/total)*errores
print ("Su puntaje final fue: "+str(correctos)+"/"+str(total))
#print ("Su porcentaje de aciertos es: ",pCorrectos," y su porcentaje de errores es: ",pErrores)
print ("Su porcentaje de aciertos es: %.2f  y su porcentaje de errores es: %.2f"%(pCorrectos,pErrores))
