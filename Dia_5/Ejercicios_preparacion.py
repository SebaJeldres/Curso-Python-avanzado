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