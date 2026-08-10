#Ejercicio de reconstruccion de biblioteca pero empleando POO

class Libro:

    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print("El libro ha sido prestado.")
        else:
            print("El libro no esta disponible.")

    def devolver(self):
        if self.disponible == True:
            print("El libro no esta prestado.")
        else:
            self.disponible = True
            print("El libro ha sido devuelto.")

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Disponible: {self.disponible}")

class Biblioteca:

    def __init__(self):
        self.biblioteca = []

    def vacia(self):
        if len(self.biblioteca) > 0:
            return True
        else:
            print("La biblioteca esta vacia.")
            return False

    def agregar_libro(self, Libro):
        (self.biblioteca).append(Libro)

    def actualizar_datos(self):
        with open("libros.txt", "w") as archivo:
            for libro in self.biblioteca:
                archivo.write(f"{libro.titulo},{libro.autor},{libro.disponible}\n")

    def eliminar_libro(self, titulo):
        for libro in self.biblioteca:
            if libro.titulo == titulo:
                (self.biblioteca).remove(libro)
                print(f"El libro {libro.titulo} se ha eliminado de la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.biblioteca:
            if libro.titulo == titulo:
                libro.mostrar_info()

    def prestar_libro(self, titulo):

            for libro in self.biblioteca:
                if libro.titulo == titulo:
                    libro.prestar()

    def devolver_libro(self, titulo):
        for libro in self.biblioteca:
            if libro.titulo == titulo:
                libro.devolver()

    def ver_biblioteca(self):
        if self.vacia():
            i = 1
            for libro in self.biblioteca:
                print(f"Libro #{i}")
                libro.mostrar_info()
                i += 1


def menu():
    print("\n------------MENU-------------")
    print("1.-Agregar libro")
    print("2.-Ver biblioteca")
    print("3.-Eliminar libro")
    print("4.-Buscar un libro")
    print("5.-Prestar un libro")
    print("6.-Devolver un libro")
    print("7.-Salir\n")

def agregar_libro(biblioteca):
    titulo = input("Ingresa el nombre del libro: ")
    autor = input("Ingresa el nombre del autor: ")

    libro = Libro(titulo,autor,True)
    biblioteca.agregar_libro(libro)
    biblioteca.actualizar_datos()

def cargar_libro(biblioteca):
    with open("libros.txt") as archivo:
        libros = archivo.readlines()

        for libro in libros:
            libro = libro.strip()
            libro = libro.split(",")
            titulol, autorl, dispol = libro
            if dispol == "True":
                dispol = True
            else:
                dispol = False
            libro = Libro(titulol,autorl,dispol)
            biblioteca.agregar_libro(libro)
        

def eliminar_libro(biblioteca):
    if biblioteca.vacia():
        titulo = input("Ingresa el nombre del libro que deseas eliminar: ")
        biblioteca.eliminar_libro(titulo)
        biblioteca.actualizar_datos()

def buscar_libro(biblioteca):
    if biblioteca.vacia():
        titulo = input("Ingresa el nombre del libro que buscas: ")
        biblioteca.buscar_libro(titulo)

def prestar_libro(biblioteca):
    if biblioteca.vacia():
        titulo = input("Ingresa el nombre del libro que quieres prestar: ")
        biblioteca.prestar_libro(titulo)
        biblioteca.actualizar_datos()

def devolver_libro(biblioteca):
    if biblioteca.vacia():
        titulo = input("Ingresa el nombre del libro que vas a devolver: ")
        biblioteca.devolver_libro(titulo)
        biblioteca.actualizar_datos()

def main():

    biblioteca = Biblioteca()
    eleccion = 0
    cargar_libro(biblioteca)

    while eleccion != 7:
       
        menu()

        try:
            eleccion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Debes ingresar un numero.")
            eleccion = 0

        match eleccion:
            case 1:
                agregar_libro(biblioteca)
            case 2:
                biblioteca.ver_biblioteca()
            case 3:
                eliminar_libro(biblioteca)
            case 4:
                buscar_libro(biblioteca)
            case 5:
                prestar_libro(biblioteca)
            case 6:
                devolver_libro(biblioteca)

        

if __name__ == "__main__":
    main()