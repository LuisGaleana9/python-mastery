#Ejercicio de reconstruccion de biblioteca pero empleando POO

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

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
        pass

    def agregar_libro()