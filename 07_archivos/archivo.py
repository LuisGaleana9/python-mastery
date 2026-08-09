#Ejercicio 1 - Uso basico
with open("saludo.txt") as archivo:
    contenido = archivo.read()

print(contenido)

#Ejercicio 2 - Guardado de libro
titulo = input("Ingresa el nombre del titulo: ")
autor = input("Ingresa el nombre del autor: ")

with open("libros.txt", "a") as archivo:
    archivo.write(f"{titulo},{autor}\n")

#Ejercicio 3 - Imprimir un archivo

with open("libros.txt") as archivo:
    contenido = archivo.readlines()

    for linea in contenido:
        print(linea)

##Ejercicio 4 - Convertir linea en libro

print("Ejercicio 4 \n")
class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_libro(self):
        print(f"{self.titulo}")
        print(f"{self.autor}")

with open("libros.txt") as archivo:
    lineas = archivo.readlines()

    for linea in lineas:
        linea = linea.strip()
        linea = linea.split(",")
        titulo, autor = linea
        libro = Libro(titulo,autor)

        libro.mostrar_libro()
