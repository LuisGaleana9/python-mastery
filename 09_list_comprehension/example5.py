numeros = [3, 7, 2, 9, 5, 8]

for x, numero in enumerate(numeros, start=1):
    if x % 2 == 0:
        print(f"Posicion {x}: {numero}")