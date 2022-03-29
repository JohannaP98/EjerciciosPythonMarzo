from random import randint
def ppt (op):
    if op==1:
        r="piedra"
    elif op==2:
        r="papel"
    elif op==3:
        r="tijera"
    return r
ganadasU = 0
ganadasM = 0
while ganadasU < 3 and ganadasM < 3:
    opUsuario = int (input("Ingrese una opción :\n1.-Piedra\n2.-Papel\n3.-Tijera\n"))
    if opUsuario>3 or opUsuario<1:
        print ("Ingrese una opción valida")
        continue
    opMaquina = randint (1,3)
    print("El usuario eligio: ",ppt(opUsuario))
    print("La maquina eligio: ",ppt(opMaquina))
    if (opUsuario == 1 and opMaquina == 3) or (opUsuario == 2 and opMaquina == 1) or (opUsuario == 3 and opMaquina == 2):
        print("Gana el usuario")
        ganadasU+=1
        if ganadasU==3:
            print("El ganador es el usuario")
    elif opUsuario == opMaquina:
        print("Es un empate")
    elif (opMaquina == 1 and opUsuario == 3) or (opMaquina == 2 and opUsuario == 1) or (opMaquina == 3 and opUsuario == 2):
        print("Gana la maquina")
        ganadasM+=1
        if ganadasM==3:
            print("El ganador es la maquina")
    print("Ganadas usuario: ",ganadasU)
    print("Ganadas maquina: ",ganadasM,"\n")
