#Buscar el valor mas alto y el mas bajo


menor = min(58,65,7657,4535,234,4)
print(menor)


lista = [1, 23, 123, 32,13, 1,3, 1,3, 123,1, 3,123 ,1,3]

print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ["Juan", "Pedro", "Jose", "Maria"]
nombre = "Sebastian"
print(min(nombres))
print(max(nombre))


dic = {"c1":45, "C2":11}

print(min(dic))


#Ejerccio 1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)

#Ejercicio 2

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)

#Ejercicio 3
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}


edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())