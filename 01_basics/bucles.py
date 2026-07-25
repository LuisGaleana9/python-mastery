#Ejercicio de bucles 1
password_real = "132"
password = input("Ingresa la contraseña: ")

while password_real != password:
    password = input("Ingresa la contraseña correcta: ")
print("Contraseña correcta, bienvenido...")

#Ejercicio de bucles 2
numero = input("Ingresa un numero para generar su tabla de multiplicar: ")
print(f"Tabla de multiplicar de {numero}")
for i in range(1,11):
    print(f"{numero} x {i} = {int(numero) * i}")
#Ejercicio de bucles 3
total_ahorrado = 0.00

for x in range(1,6):
    cantidad = input(f"Cuanto dinero ahorraste el dia {x}: ")
    total_ahorrado += float(cantidad)
print(f"En total, ahorraste {total_ahorrado} pesos.")
