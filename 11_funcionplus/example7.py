def solicitar_datos():
    nombre = input("Nombre: ")
    carrera = input("Carrera: ")
    return nombre, carrera

def guardar_alumno(nombre, carrera):
    with open("alumno.txt", "a") as archivo:
        archivo.write(f"{nombre},{carrera}\n")

def registrar_alumno():
    nombre, carrera = solicitar_datos()
    guardar_alumno(nombre, carrera)
    print("Alumno registrado correctamente.")