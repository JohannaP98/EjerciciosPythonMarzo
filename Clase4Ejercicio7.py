def imprimir (dic):
    for indice in dic:
        print ("Key: ",indice,"Vlaue: ",dic[indice])

def agregarEstudiante (dic,codigo,nombre):
    dic[codigo]=[]
    dic[codigo].append(nombre)
    dic[codigo].append([])

def agregarNota (dic,codigo,nota):
    dic[codigo][1] = nota

def prom (lista):
    suma = 0
    for item in lista:
        suma+= item
    return suma/len(lista)

dic = {}
imprimir(dic)
agregarEstudiante(dic,"001","kevin")
agregarNota(dic,"001",10)
agregarNota(dic,"001",8)
imprimir(dic)
