import random
import requests
from PIL import Image #para las fotos
from io import BytesIO #Para las fotos

api = "https://hamtaro-restapi.vercel.app/characters/list"
contenido = requests.get(api)
respuesta = contenido.json()
personaje = respuesta[random.randint(1,31)]

nombre_pers = personaje["name"]
genero = personaje["gender"]
especie = personaje["species"]
desc = personaje["description"]

foto = "https://hamtaro-restapi.vercel.app/" + personaje["image"] #para cuando no tenga el link
respuesta_IMG = requests.get(foto)
imagen = Image.open(BytesIO(respuesta_IMG.content))
imagen.show()

print(personaje)
#print(nombre_pers)

#------------------------------------------------------
print("--------Juego de Hamtaro-------------")
print("Adivina el personaje a partir de la foto:")

print(f"Pistas: Su especie es {especie} y su genero es {genero}\n"
      "(Tienes 6 intentos)")

contador = 0

personaje_oculto = [] #lista para guardar el personaje oculto
for i in range(len(nombre_pers)): #Para pasar el nombre a rayas
    personaje_oculto.append("_")

print(f"Nombre:{personaje_oculto}")

while contador < 6 and "_" in personaje_oculto:
    print(f"Intentos: {contador}")
    letra = input("Introduce una letra: ")

    if letra in nombre_pers:
        for i in range(len(nombre_pers)):
            if nombre_pers[i] == letra:
                personaje_oculto[i] = letra
                print("Correcto, letra aceptada!")
                print(f"Nombre: {personaje_oculto}")
    else:
        contador += 1
        print(f"Incorrecto!")

if "_" not in personaje_oculto:
    print(f"Has ganado, él personaje es: {desc}!")
else:
    print(f"Has perdido, él personaje era: {desc}!")



