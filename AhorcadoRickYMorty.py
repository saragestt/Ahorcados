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
      f"Adivina el personaje a partir de estas pistas: {especie}, {tipo} y {genero}. \n"
      f"Tienes 6 intentos (Los espacios cuentan como palabras)")

contador = 0

personaje_oculto = []
for i in range(len(nombre)):
    personaje_oculto.append("_")

print(f"Nombre:{personaje_oculto}")


while contador < 6 and "_" in personaje_oculto:
    print(f"Intentos: {contador}")
    letra = (input(f"Introduce una letra: "))#no me lee las mayusculas como minusculas y si le pongo .lower me salta que esta mal

    if letra in nombre:
        print("Letra correcta!")
        for i in range(len(nombre)):
            if nombre[i] == letra:
                personaje_oculto[i] = letra
                print("Nombre:"," ".join(personaje_oculto))
    else:
        contador += 1
        print("Incorrecto!")


if "_" not in personaje_oculto:
    print(f"Has ganado! El personaje oculto es: {nombre}")
else:
    print(f"Has perdido! El personaje oculto era: {nombre}")









