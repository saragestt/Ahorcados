import random
import requests


urlSimpsons = "https://thesimpsonsquoteapi.glitch.me/quotes"
respuesta = requests.get(urlSimpsons)
contenido = respuesta.json()
#print(contenido)

objeto = contenido[0]

frase = objeto["quote"]
personaje = objeto["character"]
print(personaje)

print(f"Ahorcado de los Simpsons!\n"
      f"Adivina el personaje a partir de la frase: {frase}\n"
      f"(Tienes 6 intentos)")

contador_intentos = 0

personaje_oculto = []
for i in range(len(personaje)):
    personaje_oculto.append("_")
print(personaje_oculto)

while contador_intentos < 6:
    print(f"Intentos: {contador_intentos}")
    letra = input("Introduce una letra: ")

    if letra in personaje:
        personaje_oculto[i].join(letra) #aqui no se como ponerlo para que se quiten las rayas
        print("Correcto, letra aceptada!")
        print(personaje_oculto)
    else:
        contador_intentos += 1
        print(f"Incorrecto!")

if "_" not in personaje_oculto:
    print(f"Has ganado, él personaje es: {personaje}!")
else:
    print(f"Has perdido, él personaje era: {personaje}!")






