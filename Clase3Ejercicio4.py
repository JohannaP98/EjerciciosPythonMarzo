saldo = 0
op=0
while (op!=3):
    op=int (input("Ingrese opción: \n1.-Depósito\n2.-Retiro\n3.-Salir\n"))
    if op < 0 or op > 3:
        print("Opción no valida")
        continue
    if op == 1:
        cant = float (input("Ingrese cantidad: "))
        saldo+=cant
        
    elif op == 2:
        cant = float(input("Ingrese cantidad: "))
        if cant > saldo:
            print("No puede retirar esa cantidad")
        else:
            saldo-=cant
    elif op == 3:
        print ("Saliedo...")
print ("Su saldo total es de : ",saldo)
