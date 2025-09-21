#Bucle while

#se repite hasta que se cumpla una condicion

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1

else:
    print("no tengo monedas")



respuesta = "s"

while respuesta == "s":
    respuesta = input("¿Quires continuar?: s/n")
else:
    print("Proceso finalizado")

nombre = input("Nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)

#Ejercicio 1

numero = 10

while numero >= 0:
     print(numero)
     numero -= 1

#Ejercicio 2
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

#Ejercicio 3
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero >= 0:
        print(numero)
        continue
    else:
        break