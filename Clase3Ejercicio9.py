from random import randint

def llenarSec (n):
    listaA = []
    for i in range(1,n+1):
        listaA+=[i]
    return  listaA

def llenarAle (n):
    listaB = []
    num = randint(1,n)
    listaB += [num]
    for i in range(n-1):
        while num in listaB:
            num = randint(1,n)
        listaB += [num]
    return listaB

listaA = llenarSec(10)
listaB = llenarAle(10)
for i in range (len(listaA)):
    print ("La persona: ",listaA[i], " es pareja con ",listaB[i])
print (listaA)
print (listaB)

