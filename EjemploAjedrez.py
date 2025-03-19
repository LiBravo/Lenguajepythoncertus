dimensiones= int(input("Ingrese el tamaño del tablero: "))

for i in range(dimensiones):
    for j in range(dimensiones):
        if (i+j) %2 ==0:
            print("#", end=" ")
        else:
            print(" ", end=" ")

    print()