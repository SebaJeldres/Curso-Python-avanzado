



def chequear_tres_cifras(lista):

    lista_3_cifras = []


    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_tres_cifras([555,99,600])
print(resultado)


#Ejercicio 1
def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
    return True


lista_numeros = [-23, 34, 4545, -67, 45, -23]

#Ejercicio 2
def suma_menores(lista):
    contenedor = 0
    for n in lista:
        if n > 0 and n < 1000:
            contenedor += n
    return contenedor


lista_numeros = [10, 34, 0, 324, 33]

#Ejercicio 3
def cantidad_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador



lista_numeros = [23,33,45,70,80,34,22,26,43]