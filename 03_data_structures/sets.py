#Ejercicio 1 de sets
lista = ["Tacos", "Hamburguesa", "Sushi", "Tamales", "Pizza" , "Pizza" , "Sushi"]
print(lista)
lista_set = set(lista)
print(lista_set)

#Ejercicio 2 de sets
whitelist = {"Luis", "Aleydis", "Alberto"}
whitelist.add("Joana")
whitelist.add("Luis")
whitelist.remove("Alberto")
print(whitelist)

#Ejercicio 3 de sets
juegan_fifa = {"Luis", "Emmanuel", "Angel"}
juegan_lol = {"Luis", "Junior", "Santiago"}

juegan_ambos = juegan_fifa & juegan_lol
solo_fifa = juegan_fifa - juegan_lol
print(juegan_ambos)
print(solo_fifa)
 