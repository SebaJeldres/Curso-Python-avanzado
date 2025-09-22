#Importar la libreria

from random import *

aleatorio = randint(1,50) #solo enteros

print(aleatorio)


aleatorio1 = uniform(1,50) #Enteros y decimales
print(aleatorio1)

aleatorio2 = random() #Numeros entre 0 y 1
print(aleatorio2)


lista = ["rojo", "verde", "azul"]
aleatorio3 = choice(lista) #Aleatorio de una lista
print(aleatorio3)


numeros = list(range(5,50,5))
shuffle(numeros)  #Reordena los elementos de una lista
print(numeros)

#Ejercicio 1
aleatorio = randint(1,10)

#Ejercicio 2

aleatorio = random()

#Ejercicio 3
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)
