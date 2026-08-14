from calculadora import sumar,restar,multiplicar

def main():
    numero1 = int(input("Ingresa el numero 1: "))
    numero2 = int(input("Ingresa el numero 2: "))

    suma= sumar(numero1,numero2)
    resta= restar(numero1,numero2)
    multi= multiplicar(numero1,numero2)

    print(f"Sumados: {suma}, restados: {resta}, multiplicados: {multi}")

if __name__ == "__main__":
    main()