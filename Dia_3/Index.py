#Valor del caracter de una posicion especifica
mi_texto = "Esta es una prueba"
resultado = mi_texto[9]
print(resultado)

#Posicion de un caracter
resultado1 = mi_texto.index("a")
print(resultado1)

#Busqueda con limites
resultado3 = mi_texto.index("a", 5, 11)
print(resultado3)


#Izquierda a derecha
resultado4 = mi_texto.rindex("a")
print(resultado4)

#Ejercicio 1
palabra = "ordenador"

resultado = palabra[4]
print(resultado)

#Ejercicio 2
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado = frase.index("práctica")
print(resultado)

#Ejercicio 3
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado = frase.rindex("práctica")
print(resultado)

