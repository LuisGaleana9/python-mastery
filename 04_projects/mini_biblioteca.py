#Ejercicio de biblioteca con funciones basicas. #2

eleccion = 0
j = 0
libros = []

while eleccion != 5:
    print("\n1.-Ver libros")
    print("2.-Agregar libros")
    print("3.-Buscar libro")
    print("4.-Eliminar libro")
    print("5.-Salir\n")
    eleccion = int(input("Elige una opcion valida: "))

    match eleccion:
        case 1:
            if not libros:
                print("No hay libros aun.")
            else:
                print("Lista de libros:")
                i = 1
                for libro in libros:
                    print(f"Libro #{i}")
                    print(f"Titulo: {libro['titulo']}")
                    print(f"Autor: {libro['autor']}")
                    print(f"Disponible: {libro['disponible']}")
                    i += 1

        case 2:
            titulo = input("Escribe el titulo del libro: ")
            autor = input("Escribe el nombre del autor: ")
            while 1:
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

        case 3:
            if not libros:
                print("La biblioteca esta vacia.")
            else:
                buscar = input("Ingresa el nombre del libro que buscas: ")
                for libro in libros:
                    if libro["titulo"] == buscar:
                        print("Resultado:")
                        print(f"Titulo: {libro['titulo']}")
                        print(f"Autor: {libro['autor']}")
                        print(f"Disponible: {libro['disponible']}")
                    print("Intenta con otro nombre.")

        case 4:
            if not libros:
                print("La biblioteca esta vacia.")
            else:
                print("La biblioteca esta vacia.")
                buscar = input("Ingresa el nombre del libro que deseas eliminar: ")
                i = 1
                for libro in libros:
                    if libro["titulo"] == buscar:
                        del libros[i-1]
                        print("Libro eliminado.")
                        break
                print("Intenta con otro nombre.")

        case _:
            print("Elige una opcion valida...\n")