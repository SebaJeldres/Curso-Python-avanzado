# *args = argumentos de una funcion
#Las funciones por defecto solo se pueden pasar la cantidad señalada de argumentos
#Con *args el numero de parametros sea variable


def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(5,6,5,4,3,3,2,2,2,34,5,6,45,4,5,4))


#Ejercicio 1
def suma_cuadrados(*args):
    total = 0

    for arg in args:
        total += arg ** 2

    return total

#Ejercicio 2
def suma_absolutos(*args):
    total = 0
    for arg in args:
        total += abs(arg)
    return total

#Ejercicio 3
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"