hora = 20
minutos = 59
segundos = 59
print ("La hora es: ",hora,":",minutos,":",segundos)
if hora <= 23 and minutos == segundos <=59:
    segundos+=1
    if segundos == 60:
        minutos+=1
        segundos=0
    if minutos ==60:
        hora +=1
        minutos=0
    if hora == 24:
        hora=0
    print ("La hora un segundo despues es: ",hora,":",minutos,":",segundos)
else:
    print("Ingrese un hora valida")