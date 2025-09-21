# bucles
# iterables: listas, tuplas, diccionarios

#Loop for

lista = [1,2,3,4,5]

for i in lista:
    numero_numero = lista.index(i) + 1
    print("Numero: ",numero_numero, i)





lista1 = ["luis","pablo", "fede","laura","julia"]

for nombre in lista1:
    if nombre.startswith("l"):
        print(nombre)
    else:
        print("nombre que no inicia con l", nombre)


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)


palabra = "python"

for letra in palabra:
    print(letra)


dic ={"clave1": "a", "clave2": "b", "clave3": "c" }
for item in dic.values():
    print(item)

#Ejercicio 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print(f"Hola {nombre}")

#Ejercicio 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for num in lista_numeros:
    suma_numeros = suma_numeros + num

#Ejercicio 3

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero