texto = "Este es el texto de sebastian"


resultado = texto. upper()
print(resultado)

resultado2 = texto[2].upper()
print(resultado2)

resultado1 = texto.lower()
print(resultado1)

resultado3 = texto.split()
print(resultado3)

resultado4 = texto.split("t")
print(resultado4)

a = "aprender"
b = "Python"
c = "Es"
d = "Genial"
e = " ".join([a, b, c, d])

print(e)

resultado5 = texto.find("texto")
print(resultado5)

resultado6 = texto.replace("texto", "arco")
print(resultado6)

#ejercicio 1
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

print(frase.upper())

#Ejercicio 2
lista_palabras = ["La","legibilidad","cuenta."]

resultado = " ".join(lista_palabras)
print(resultado)

#Ejercicio 3
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

a = frase.replace("difícil", "fácil")
b = a.replace("mala", "buena")

print(b)