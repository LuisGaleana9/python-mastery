cuadrado = lambda numero: numero * numero

print(cuadrado(5))   

#2

personas = [
    {"nombre": "Luis", "edad": 23},
    {"nombre": "Ana", "edad": 21},
    {"nombre": "Carlos", "edad": 25}
]

personas_ordenadas =    sorted(personas, key= lambda mayor: mayor["edad"], reverse= True)

print(personas_ordenadas)

#FILTER

numeros = [3, 8, 12, 5, 20, 7, 10]

resultado = list(filter(lambda numero: numero > 7, numeros))
print(resultado)


#MAP

nombres = ["luis", "ana", "carlos", "pedro"]
resultado = list(map(lambda nombre: nombre.upper(), nombres))
print(resultado)

#2

personas = [
    {"nombre": "Luis", "edad": 23},
    {"nombre": "Ana", "edad": 21},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Pedro", "edad": 19}
]

resultado = list(map(lambda nombre: nombre["nombre"].upper(), list(filter(lambda persona: persona["edad"] > 21, personas))))
print(resultado)