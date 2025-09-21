#Rangos
#rango de numeros

#Primer valor: define el inicio del rango
#Segundo valor: define el fin del rango
#Tercer valor: define los saltos que dara la iteracion
#Solo numeros enteros

for numero in range (1,5,2):
    print(numero)

#Lista de numeros
lista = list(range(1, 101))
print(lista)

#Ejercicio 1

mi_lista = list(range(2500, 2586))

#Ejercicio 2

mi_lista = list(range(3, 301, 3))

#Ejercicio 3
suma_cuadrados = 0

for numero in range (1,16):
    num = numero ** 2
    suma_cuadrados *= num