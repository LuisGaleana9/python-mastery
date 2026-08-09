# Ejercicio 1 TRY 

try:
    numero = int(input("Ingresa un numero: "))
    print(100 / numero)
except ValueError:
    print("Debes ingresar un numero valido.")
except ZeroDivisionError:
    print("No puedes dividir sobre 0")

#EJERCICIOS 2 
try:
    numero = int(input("Número: "))
except ValueError:
    print("No es un número.")
else:
    print("Conversión exitosa.")
    print(numero * 2)   

#Ejercicio 3

try:
    print("Abriendo programa...")
    int(input("Ingresa un numero: "))
except ValueError:
    print("Ha ocurrido un error.")  
finally:
    print("El programa se cerro.")

##Ejercicio 4

try:

    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        raise ValueError("Debes ingresar tu edad real...")  

    print("Perfecto.")

except ValueError as error:
    print(error)

