def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_info(nombre="Luis", edad=23, carrera="Ingeniería en Computación")