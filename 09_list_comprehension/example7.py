nombres = ["Luis", "Aleydis", "Alberto", "Carlos"]
edades = [23, 21, 20, 25]

personas_mayores = [(nombre, edad) for nombre, edad in zip(nombres,edades) if edad > 21]

print(personas_mayores)