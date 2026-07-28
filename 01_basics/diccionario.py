#Ejercicio diccionario 1
server_config = {"ip" : "192.168.7.140", "puerto" : 48055, "max_p" : 4}
print(f"Deben conectarse a la ip: {server_config["ip"]}:{server_config["puerto"]}")

#Ejercicio diccionario 2
aldea = {"ayunta" : 18, "medallas" : 250}
aldea["liga"] = "campeones 3"
aldea["medallas"] += 50

print(aldea)
#Ejercicio diccionario 3
estadisticas = {"messi" : 20 , "ronaldo" : 10, "haaland" : 19}
for jugador,goles in estadisticas.items():
    print(jugador,goles)
