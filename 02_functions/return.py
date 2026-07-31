#Ejercicio 1

def calcular(a,b):
    """
    Recibe 2 numero y regresa su suma,resta,multiplicacion y division.
    """
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b

    return suma,resta,multi,div

suma, resta, multi, div = calcular(50,30)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multi}")
print(f"Division: {div}")

print(calcular.__doc__)

#Ejercicio 2
numeros = [5,10,15,20,25,30]
primero, *medio, ultimo = numeros
print(primero)
print(medio)
print(ultimo)