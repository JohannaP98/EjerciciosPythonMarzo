lista = [1,"hola",3.5,False]

while len(lista)>0:
    print (lista)
    elementos = int (input("Ingrese la posición del elemento a eliminar\n"))
    if elementos >len(lista)-1:
        print("El elemento esta fuera del rango")
        continue
    del(lista[elementos])