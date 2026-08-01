#Ejercicio de biblioteca con funciones basicas. #2

def mostrar_menu():
    print("\n1.-Ver libros")
    print("2.-Agregar libros")
    print("3.-Buscar libro")
    print("4.-Eliminar libro")
    print("5.-Salir\n")

def hay_libros(libros):
    """
    Funcion para ver si hay libros en la biblioteca
    """
    if not libros:
        print("No tienes libros en la biblioteca aun.")
        return False
    return True

def ver_libros(libros):
    """
    Funcion para listar los libros que hay, si es que hay. 
    Recibe la lista de libros.
    """
    if hay_libros(libros):
        print("Lista de libros:")
        for i, libro in enumerate(libros, start=1):
            print(f"Libro #{i}")
            mostrar_libro(libro)

def agregar_libro(libros):
    """
    Funcion para agregar libros a la lista de libros
    """
    titulo = input("Escribe el titulo del libro: ")
    autor = input("Escribe el nombre del autor: ")

    while True:
        disponible = input("Hay disponibilidad?(si o no): ").lower()
        if disponible == "si":
            disponible = True
            break
        elif disponible == "no":
            disponible = False
            break
        else:
            print("Error, responde si o no.\n")

    libros.append({"titulo" : titulo, "autor" : autor, "disponible" : disponible})

def buscar_libro(libros):
    """
    Funcion para buscar libros con el nombre
    """
    encontrado = False
    if hay_libros(libros):
        buscar = input("Ingresa el nombre del libro que buscar: ")
        for libro in libros:
            if libro['titulo'] == buscar:
                print("Resultado:")
                mostrar_libro(libro)
                encontrado = True
        if not encontrado:
            print("Intenta con otro nombre.")

def eliminar_libro(libros):
    """
    Funcion para eliminar un libro de la biblioteca
    """
    if hay_libros(libros):
        buscar = input("Ingresa el nombre del libro que deseas eliminar: ")
        encontrado = 0
        i = 1
        for libro in libros:
            if libro['titulo'] == buscar:
                del libros[i-1]
                print("Libro eliminado.")
                encontrado = True
            i += 1
        if not encontrado:
            print("No esta el libro que quieres eliminar.")

def mostrar_libro(libro):
    print(f"Titulo: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Disponible: {libro['disponible']}")


def main():
    eleccion = 0
    j = 0
    libros = []

    while eleccion != 5:
        mostrar_menu()
        eleccion = int(input("Elige una opcion valida: "))

        match eleccion:
            case 1:
                ver_libros(libros)

            case 2:
                agregar_libro(libros)

            case 3:
                buscar_libro(libros)

            case 4:
                eliminar_libro(libros)

            case _:
                print("Elige una opcion valida...\n")

if __name__ == "__main__":
    main()