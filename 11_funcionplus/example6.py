productos = [
    {"nombre": "laptop", "precio": 1200, "stock": 5},
    {"nombre": "mouse", "precio": 25, "stock": 0},
    {"nombre": "teclado", "precio": 45, "stock": 10},
    {"nombre": "monitor", "precio": 300, "stock": 2},
    {"nombre": "cable hdmi", "precio": 10, "stock": 50}
]

productos_approve = [producto["nombre"].upper() for producto in productos if producto["stock"] > 0 and producto["precio"] > 30]

print(productos_approve)