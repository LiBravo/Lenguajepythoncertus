def suma (number1,number2):
    return number1 + number2

def resta (number1,number2):
    return number1 - number2

def multiplicacion (number1,number2):
    return number1 * number2

def division (number1,number2):
    if (number2 ==0):
        print("ERROR")
    else:
        return number1/number2

ejecutar = True

while True:

    print("\nSeleccione una opcion")
    print("---------------------")
    print("1. suma +")
    print("2. resta -")
    print("3. multiplicacion x")
    print("4. division /") 
    print("5. salir")  
    print("Ingrese la operación que se desea realizar:  ")             
    
    operacion= int(input())  
    if (operacion != 5 and operacion < 6):
        number1=int(input("Ingresa el primer numero:   "))
        number2=int(input("Ingresa el segundo numero:   ")) 

    if operacion==1:
        print(f"resultado = {suma (number1, number2)}")

    elif operacion==2:
        print(f"resultado = {resta (number1, number2)}")

    elif operacion==3:
        print(f"resultado = {multiplicacion (number1, number2)}")

    elif operacion==4:
        print(f"resultado = {division (number1, number2)}")
    else:
        print("Hasta luego xD!!")
        ejecutar=False


