
#Clase 1

class libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Disponible: {self.disponible}")

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True

libro1 = libro("Habitos Atomicos", "James Clear")
libro2 = libro("Harry Potter", "J.K")

libro1.mostrar_info()
libro1.prestar()
libro1.mostrar_info()

#Clase 2

class Cuenta:

    def __init__(self, saldo):
        self._saldo = saldo

    def consultar_saldo(self):
        print(f"Tu saldo es de: {self._saldo}")

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad < self._saldo:
            self._saldo -= cantidad
        else:
            print("Saldo insuficiente.")


cuenta = Cuenta(1000)
cuenta.consultar_saldo()
cuenta.depositar(500)
cuenta.consultar_saldo()
cuenta.retirar(200)
cuenta.consultar_saldo()
cuenta.retirar(5000)

#Herencia

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre,edad)
        self.carrera = carrera

alumno1 = Alumno("Luis",23,"Computacion")
print(alumno1.nombre)
print(alumno1.edad)
print(alumno1.carrera)