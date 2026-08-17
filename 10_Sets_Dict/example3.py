## Imprimir especificos
usuario = {
    "nombre": "Luis",
    "edad": 23,
    "lenguajes": ["Python", "C++", "Java"],
    "experiencia": "Junior"
}
claves_mostrar = {"nombre", "experiencia"}

for clave, valor in usuario.items():
    if clave in claves_mostrar:
        print(f"{clave}: {valor}")