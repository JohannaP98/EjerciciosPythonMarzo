altura = 5
espacios = altura
carac = 1
for i in range (altura):
    for j in range (espacios):
        print (" ",end="" )
    for k in range (carac):
        print ("* ",end="")
    carac+=1
    espacios-=1
    print()
        