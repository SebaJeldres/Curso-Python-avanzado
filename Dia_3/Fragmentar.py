texto = "ABCDEFGHIJKLM"

#Tomar fragmento de una cadena de texto
fragmento = texto[2 : 5]
print(fragmento)

#Tomar fragmento con un iniio asignado hasta el final
fragmento1 = texto[2 :]
print(fragmento1)

#Tomar fragmento, pero con salto de caracteres
fragmento2 = texto[2:10:3]
print(fragmento2)

#Negativos voltean la cadena o inician desde el ultimo caracter
fragmento3 = texto[::-1]
print(fragmento3)

#Ejercicio 1
frase = "Controlar la complejidad es la esencia de la programación"

fragmento = frase[: 9]
print(fragmento)

#ejercicio 2
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

fragmento = frase[8 : : 3]
print(fragmento)

#Ejercicio 3
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

fragmento = frase[::-1]
print(fragmento)