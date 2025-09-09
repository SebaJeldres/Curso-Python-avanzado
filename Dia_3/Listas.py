#Listas

#cualquier tipo de datos

#Metodos iguales a los strings
mi_lista = ["a","b","c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista)
print(mi_lista2)

print(type(mi_lista))
print(type(mi_lista2))

resultado = len(mi_lista)
print(resultado)

resultado2 = mi_lista2[0]
print(resultado2)

print(mi_lista3)

mi_lista3[0] = "alfa"
print(mi_lista3)

mi_lista3.append("g")
print(mi_lista3)


eliminado = mi_lista3.pop()
print(mi_lista3)
print(eliminado)

#Metodos para las listas

#ordena la lista (No guarda el orden)
lista = ["g", "o", "f", "H", "e", "z"]
lista.sort()
print(lista)

#reversiona la lista
lista.reverse()
print(f"Esta lista es {lista}")

#Ejercicio 1
mi_lista = ["3", "4", 5, 5, 6]

#Ejercicio 2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]

medios_transporte.append("motocicleta")
print(medios_transporte)

#Ejercicio 3
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

eliminado = frutas.pop(2)
print(eliminado)

