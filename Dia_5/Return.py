#Retorna el resultado, en vez de retornar solo un print, nos sirve para guardar el valor

def multiplicar(num1, num2):
    return num1 * num2

multiplicar(1, 2)

resultado = multiplicar(1, 2)
print(resultado)

#Ejercicio 1
def potencia(num1,num2):
    total = num1 ** num2
    return total

#Ejercicio 2
def usd_a_eur(dolares):
    return dolares * 0.90


dolares = 98

usd_a_eur(dolares)

#Ejercicio 3
def invertir_palabra(palabra):
    return palabra[::-1].upper()


palabra = "Sebastian"