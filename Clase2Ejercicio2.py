from random import randint

zonaUsuario = 3
zonaPortero = randint(1,6)

print ("La zona cubierta por el portero es: ",zonaPortero)

if zonaUsuario == zonaPortero:
    print ("No ha sido un gol")
else:
    print("Gooool")

#randint (x,y)              número aleatorio entero entre "x" y "y"
#random()                   número aleatorio entre 0 y 1
#randrange(x,y,p)           número aleatorio entero emtre "x" y "y" con un paso de "p"
#uniform(x,y)               número aleatorio de tipo float entre "x" y "y" 