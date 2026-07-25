#Ejercicio de condicionales 1
estatura = float(input("Ingresa tu estatura(en metros): "))
if estatura >= 1.50:
    print("Puedes ingresar a la montaña rusa!")
else:
    print("No tienes la estatura necesaria para ingresar a la montaña rusa :(")

#Ejercicio de condicionales 2
edad = int(input("Ingresa tu edad: "))
if edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente.")
elif edad > 17 and edad < 60:
    print("Eres un Adulto.")
else:
    print("Eres un adulto mayor.")

#Ejercicio de condicionales 3
usuario = "luisgaleana"
password = "123"

user = input("Ingresa tu usuario: ")
passw = input("Ingresa tu contraseña: ")
if user == usuario and passw == password:
    print("Acceso concedido. Bienvenido...")
else:
    print("Acceso denegado. Credenciales incorrectas.")