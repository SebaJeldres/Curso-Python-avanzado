#Ejercicio 1
def devolver_distintos(num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    suma = sum(lista_numeros)

    if suma > 15:
        return max(lista_numeros)
    elif suma < 10:
        return min(lista_numeros)
    else:
        return sorted(lista_numeros)[1]


resultado = devolver_distintos(45, 34, 2)
print(resultado)


#Ejercicio 2
#Devolver letras de una palabra sin repetidos y en orden alfabetico

def palabra(palabra):
    letras = set(palabra)
    lista = sorted(letras)
    return lista


print(palabra("zapallo"))

#Ejercicio 3

def busqueda(*lista):

    conteo = 0

    for n in lista:
        if n == 0:
            conteo += 1
    return conteo > 1

print(busqueda(2,34,45,56,67,0,65,344,43,23))


#Ejercicio 4

def contar_primos(n):
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)

    print("Números primos encontrados:", primos)
    return len(primos)


print("Cantidad de primos:", contar_primos(30))
