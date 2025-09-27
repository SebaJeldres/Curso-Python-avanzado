#El ahorcado
# una palabra al azar
# Se le meustra al usuario las lineas por cada letra de la palabra
# 6 vidas
# si acierta una letra se debe mostrar en la secuencia


from random import choice

lista_palabras = ["casa", "perro", "libro", "cielo", "mar", "sol", "computadora", "flor", "camino", "amigo"]
palabra_secreta = choice(lista_palabras)
vidas = 6


def mostrar_lineas(palabra_secreta, letras_adivinadas):
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado



letras_adivinadas = []

while vidas > 0:
    print("\n" + mostrar_lineas(palabra_secreta, letras_adivinadas))
    letra = input("Adivina una letra: ").lower()

    if letra in palabra_secreta and letra not in letras_adivinadas:
        letras_adivinadas.append(letra)
        print("¡Bien! Has acertado una letra.")
    elif letra in letras_adivinadas:
        print("Ya habías adivinado esa letra.")
    else:
        vidas -= 1
        print(f"Incorrecto. Te quedan {vidas} vidas.")

    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
        break

if vidas == 0:
    print(f"Has perdido. La palabra era: {palabra_secreta}")

