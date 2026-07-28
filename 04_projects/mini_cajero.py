#Ejercicio de Cajero automatico con funciones basicas. #1

opcion = 0
saldo = 0

while opcion != 4: 
    print("\nBienvenido a tu cajero automatico.\n")
    print("1.- Consultar saldo")
    print("2.- Depositar saldo")
    print("3.- Retirar dinero")
    print("4.- Salir")
    opcion = int(input("Ingresa una opcion: "))

    match opcion:
        case 1: 
            print(f"Tu saldo es de {saldo}")
        case 2:
            saldo += int(input("Cuanto saldo deseas ingresar a tu cuenta de banco: "))
        case 3:
            if saldo == 0:
                print("No tienes saldo.")
            else:
                print(f"Tu saldo disponible es de {saldo}")
                retiro = int(input("Cuanto dinero deseas retirar?: "))
                if retiro > saldo:
                    print(f"No tienes ese saldo disponible. Tienes {saldo}")
                else:
                    saldo -= retiro
        case 4: 
            print("Hasta luego.")
        case _:
            print("Elige una opcion valida.")
