usuarios = [
    {"nombre": "Luis", "edad": 23},
    {"nombre": "Ana", "edad": 21},
    {"nombre": "Carlos", "edad": 25}
]

for usuario in usuarios:
    if usuario["edad"] > 21:
        print(f"{usuario["nombre"]}")