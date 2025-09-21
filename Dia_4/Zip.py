#Llega hasta el dato de la fila mas corta
#Entrelaza los valores de listas distintas (2 o mas)


nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42]
ciudades = ["Santiago","Madrid","Lima"]

combinados = list(zip(nombres, edades, ciudades))

print(combinados)



for nombre, edade, ciudad in combinados:
    print(f"{nombre} tiene {edade} y vive en: {ciudad}")


#Ejercicio 1

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales, paises))

for capital, pais in combinados:
    print(f"La capital de {pais} es {capital}")


#Ejercicio 2
marcas = ["Toyota", "Nissan"]
productos = ["AE86", "Skyline"]

mi_zip = zip(marcas, productos)


#Ejercicio 3
# Listas de números en los tres idiomas
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

# Creamos el zip y lo convertimos en lista
numeros = list(zip(espanol, portugues, ingles))

print(numeros)
