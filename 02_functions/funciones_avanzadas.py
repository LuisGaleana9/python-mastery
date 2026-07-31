#Ejercicio 1 fun_avanzadas

def registrar_usuario(nombre,edad,ciudad="Morelia"):
    print("Usuario registrado: \n" \
    f"Nombre: {nombre}\n" \
    f"Edad: {edad}\n" \
    f"Ciudad: {ciudad}")

#registrar_usuario(nombre= "Luis", ciudad="Petatlan", edad=23)
#registrar_usuario("Alberto",23)

#Ejercicio 2 *ARGS

def imprime(*args):
    print(args)

imprime(23, "Hola", "Adios", True)

#Ejercicio 3 *ARGS

def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)

sumar(10,100,30,500,10)

#Ejercicio 4 (*args)

def promedio(*args):
    total = 0

    for numero in args:
        total += numero/len(args)
    print(f"El promedio es de: {total}")

numeros = []
long = int(input("Cuantos numeros vas a ingresar?: "))
for x in range(long):
    numeros.append(int(input(f"Ingresa el numero {x+1}: ")))

promedio(*numeros)
    
#Ejercicio 5 (**KWARGS)

def perfil(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave}:", f"{valor}")

perfil(Nombre= "Luis", Edad=23, Carrera= "Ingeniero")