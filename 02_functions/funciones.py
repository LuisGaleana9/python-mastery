#Ejercicio de funciones 1
def calcular_descuento(precio,porcentaje_descuento):
    print(f"El precio original es {precio} y con un descuento de {porcentaje_descuento}, el precio final seria de {precio - precio*porcentaje_descuento/100}")

precio = int(input("Ingresa el precio: "))
descuento = int(input("Ingresa el descuento (en porcentaje): "))
calcular_descuento(precio,descuento)

#Ejercicio de funciones 2
def verificacion(edad):
    """"
    Regresa True si tu edad es mayor o igual a 18
    """
    if edad >= 18:
        return True
    else :
        return False

if verificacion(edad = int(input("Ingresa tu edad: "))) == True:
    print("Acceso aprobado!")
else:
    print("Acceso denegado!")

#Ejercicio de funciones 3

def total_medallas(estrellas, bono_liga = 50):
    """
    Hace el calculo de tu total de medallas apartir de tus estrellas y tu bono de liga que puedes ingresar opcionalmente.
    """
    return estrellas * 10 + bono_liga

estrellas = int(input("Ingresa las estrellas conseguidas: "))
print(f"Tus estrellas totales con un bono de 50, son: {total_medallas(estrellas)}")

estrellas = int(input("Ingresa las estrellas conseguidas: "))
bono = int(input("Ingresa tu bono: "))
print(f"Tus estrellas totales son: {total_medallas(estrellas,bono)}")

print(total_medallas.__doc__)