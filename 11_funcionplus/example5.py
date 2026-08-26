from functools import reduce

productos = [
    {"nombre": "laptop", "precio": 1200, "stock": 5},
    {"nombre": "mouse", "precio": 25, "stock": 0},
    {"nombre": "teclado", "precio": 45, "stock": 10},
    {"nombre": "monitor", "precio": 300, "stock": 2},
    {"nombre": "cable hdmi", "precio": 10, "stock": 50}
]

resultado = reduce(lambda acumulador, actual: acumulador + " | " + actual, list(map(lambda p: p["nombre"].upper(), list(filter(lambda p: p["precio"] > 30 and p["stock"] > 0, productos)))))

print(resultado)