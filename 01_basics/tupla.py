#Ejercicio de tupla 1
spawn_point = (10,50,45)
print(spawn_point)
print(f"La altura de la aparicion es de {spawn_point[1]}")

#Ejercicio de tupla 2

#Desempaquetado : Puedes extraer multiples valores y asignarlo a muchas variables a la vez en una sola linea
ticket = (200, 5.5)
monto, cuota = ticket
print(f"Por un monto de {monto} con una cuota de {cuota}, obtendrias {monto*cuota} ")

#Ejercicio 3 de tupla

def analisis_partido (goles_chivas, goles_rival):
    dif_goles = abs(goles_chivas-goles_rival)
    x = goles_chivas > goles_rival

    return dif_goles,x

analisis = analisis_partido (4,2)
print(analisis)
        
