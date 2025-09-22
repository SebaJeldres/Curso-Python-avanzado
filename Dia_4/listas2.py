#comprension de listas

palabra = "python"

lista=[]

for letra in palabra:
    lista.append(letra)

palabra1 = "Zapato"

lista2 = [letra for letra in palabra1]
print(lista2)


#Variables de tipos de listas

#Ejercicio 1
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [numero ** 2 for numero in valores]

#Ejercicio 2
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [numero for numero in valores if numero % 2 == 0 ]

#Ejercicio 3
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(grados - 32) * (5/9) for grados in temperatura_fahrenheit]

