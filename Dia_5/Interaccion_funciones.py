# Lista inicial
# mezclar palitos
# pedirle intento
# comprobar intento

from random import shuffle

palitos = ["-", "--", "---", "----"]

def mezclar(lista):
    shuffle(lista)
    return lista

def probar_suerte():
    intento = ""

    while intento not in ["1","2","3","4"]:
        intento = input("Ingrese el numero de la suerte: ")

    return int(intento)

def chequear_intento(lista,intento):
    if lista[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te haz salvado")

    print(f"Te ha tocado {[lista[intento - 1]]}")



palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


#Ejercicio 1
from random import randint


def lanzar_dados():
    # Generamos dos números entre 1 y 6
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    return n1, n2


def evaluar_jugada(n1, n2):
    suma_dados = n1 + n2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

#Ejercicio 2

lista_numeros = [1, 23, 34, 44, 44, 55, 66, 66, 2, 1, 657]


def reducir_lista(lista):
    lista = list(set(lista))

    lista.remove(max(lista))

    return lista


def promedio(lista):
    contador = 0
    suma = 0
    for n in lista:
        contador += 1
        suma += n

    promedio = suma / contador
    return promedio


#Ejercicio 3
from random import choice


def lanzar_moneda():
    monedas = ["Cara", "Cruz"]
    resultado = choice(monedas)
    return resultado


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def probar_suerte(resultado, lista):
    if resultado == "Cara":
        print(f"La lista se autodestruira")
        lista.clear()

    else:
        print("La lista fue salvada")

    return lista