#Ejercicio de Cajero automatico con funciones basicas. #1
#Actualizacion de Cajero automatico con buenas practicas.

def menu():
    """
    Desplega el menu para el usuario.
    """
    print("\nBienvenido a tu cajero automatico.\n")
    print("1.- Consultar saldo")
    print("2.- Depositar saldo")
    print("3.- Retirar dinero")
    print("4.- Salir")

def consultar_saldo(saldo):
    """
    Funcion para consultar el saldo disponible en la cuenta
    """
    print(f"Tu saldo es de {saldo}")

def depositar_saldo(saldo):
    """
    Funcion para depositar saldo 
    Recibe saldo,deposito.
    """
    deposito = int(input("Cuanto saldo deseas ingresar a tu cuenta de banco: "))
    return saldo + deposito

def retirar_saldo(saldo):
    """
    Funcion para retirar saldo
    Recibe saldo,retiro
    """
    retiro = int(input("Cuanto dinero deseas retirar?: "))
    if puede_retirar(saldo,retiro):
        return saldo - retiro
    return saldo

def verificar_saldo(saldo):
    """
    Funcion que recibe saldo para verificar si tienes saldo mayor a 0
    """
    if saldo == 0:
        print("No tienes saldo disponible.")
        return False
    return True

def puede_retirar(saldo, retiro):
    """
    Funcion que valida si tu saldo es mayor a la cantidad que quieres retirar
    """
    if saldo < retiro:
        print("No tienes suficiente saldo para retirar.")
        return False
    else:
        return True
    

def main():
    """
    Funcion main que corre todo el programa.
    """
    opcion = 0
    saldo = 0

    while opcion != 4: 
        menu()
        opcion = int(input("Ingresa una opcion: "))

        match opcion:
            case 1: 
                consultar_saldo(saldo)
            case 2:
                saldo = depositar_saldo(saldo)
                consultar_saldo(saldo)
            case 3:
                if verificar_saldo(saldo):
                    saldo = retirar_saldo(saldo)
                    consultar_saldo(saldo)
            case 4: 
                print("Hasta luego.")
            case _:
                print("Elige una opcion valida.")

if __name__ == "__main__":
    main()