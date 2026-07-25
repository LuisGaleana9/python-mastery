#Ejercicios de variables 1
manzana = 12.50
pan = 25.00
leche = 18.20

suma = manzana + pan + leche
descuento = suma - suma * 0.10
print("El precio seria " + str(suma))
print("Con un descuento de 10% quedaria en " + str(descuento))

#Ejercicios de variables 2
nombre = input("Ingresa tu nombre: ")
anio = input("Ingresa tu año de nacimiento: ")
edad= 2026 - int(anio)
print("Hola " + nombre + " este año cumples " + str(edad)) 

#Ejercicios de variables 3
minutos = int(input("Ingresa los minutos que quieras convertir: "))
print("En horas seria " + str((minutos//60)) + " con " + str(minutos%60) + " minutos")

#Ejercicio de variables 4
a = "Agua"
b = "Aceite"

c = a
a = b
b = c

