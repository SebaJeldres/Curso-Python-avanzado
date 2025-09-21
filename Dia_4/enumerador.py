#acceder de manera mas facil al indice de una lista (ej)

lista = ["a", "b", "c", "d", "e", "f", "g", "h"]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1


for item in enumerate(lista):
    print(item)


for item in enumerate(range(23,81)):
    print(item)

#Ejercicio 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
indice = 0

for nombre in lista_nombres:
    print(f'{nombre} se encuentra en el índice {indice}')
    indice += 1


#ejercicio 2

lista_indices = []

for item in enumerate("Python"):
    print(item)
    lista_indices.append(item)

print(lista_indices)

#Ejercicio 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)