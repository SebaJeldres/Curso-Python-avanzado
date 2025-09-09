#input
#ingresa 3 letras a eleccion


texto = input("Ingrese un texto")
texto.lower()

letras = input("Ingrese 3 letras")
letras.lower()

Lista = list(letras)
lista_texto = list(texto)

#analisis

print("\n")
print("Cuantas veces aparece la letra que eligio")
print("\n")

busqueda1 = texto.count(Lista[0])
print(f"La letra {Lista[0]} tiene {busqueda1} en el texto")
busqueda2 = texto.count(Lista[1])
print(f"La letra {Lista[1]} tiene {busqueda2} en el texto")
busqueda3 = texto.count(Lista[2])
print(f"La letra {Lista[2]} tiene {busqueda3} en el texto")

print("\n")
print("Cuantas veces aparece la letra")
print("\n")

palabras = len(Lista)

print(f"El texto {texto} tiene {palabras} palabras en el texto")

print("\n")
print("Primera y ultima letra")
print("\n")

primera = lista_texto[0]
ultima = lista_texto[-1]
print(f"La primera letra es {primera} y {ultima} la ultima del texto")

print("\n")
print("Texto a la inversa")
print("\n")

lista_texto.reverse()
texto_invertido = ' '.join(lista_texto)
print(texto_invertido)

print("\n")
print("Python esta dentro del texto?")
print("\n")

respuesta = "python" in texto
dic = {True: "si", False: "no"}
print(f"La palabra python {dic[respuesta]} esta en el texto")