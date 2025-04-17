import random
import image
import requests

apiRickyMorty = "https://rickandmortyapi.com/api/character/"
personaje = random.randint(1, 826)
contenidoWeb = requests.get(f"{apiRickyMorty}{personaje}")
personaje = contenidoWeb.json()
#print(personaje)

objeto = personaje

nombre = objeto["name"]
especie = objeto["species"]
tipo = objeto["type"]
genero = objeto["gender"]
foto = objeto["image"]

print(nombre)




print(f"Ahorcado de Rick y Morty!\n"
      f"Adivina el personaje a partir de estas pistas: {especie}, {tipo} y {genero} \n"
      f"Tienes 6 intentos")

personaje_oculto = []
for i in range(len(personaje)):
    personaje_oculto.append("_")
print(personaje_oculto)

contador = 0
introduce = input(f"Introduce una letra: ")

while contador < 6:
    print(f"Intentos: {contador}")
    letra = input(f"Introduce una letra: ")

    if letra in personaje:
        print("Letra correcta!") #No se porque esto no se imprime
        print(personaje_oculto)

    else:
        contador += 1
        print("Incorrecto!") #no se porque aveces cuenta como error algunas letras que estan en el nombre y otras veces no


if "_" not in personaje_oculto:
    print(f"Has ganado! El personaje oculto es:{nombre}")
else:
    print(f"Has perdido! El personaje oculto era: {nombre}")









