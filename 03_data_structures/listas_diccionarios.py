#Ejercicio de listas 1 
inventario = ["espada","pico","antorcha"]
inventario.append(input("Ingresa un nuevo item a tu inventario: "))

print(inventario[1])
print("Inventario completo...")
for x in inventario:
    print(x)

#Ejercicio de diccionarios 1
jugador = {"nombre" : "Luis", "nivel" : int("23"), "equipo" : "azul"}
jugador["nivel"] += 1

print(f"Tu nombre es {jugador["nombre"]} y tu nivel de campeon es {jugador["nivel"]}")

#Ejercicio de lista y diccionario 1
compras = [
    {"articulo" : "playera" , "precio" : 150}, 
    {"articulo" : "zapatos" ,"precio" : 250}
    ]
total = 0

for producto in compras:
    total += producto["precio"]
print(f"El total seria de {total}")