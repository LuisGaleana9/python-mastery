def presentar(*args, **kwargs):
    print("Lenguajes:")
    for valor in args:
        print(valor)

    print("Informacion")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

presentar("Python", "C", "Java" , nombre = "Luis", edad = 23)