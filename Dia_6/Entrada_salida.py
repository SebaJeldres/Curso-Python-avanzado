#Se pueden usar todos los metodos correspondientes a strings, ademas de recorrerlas con ciclos


#Abrir un archivo
mi_archivo = open("prueba.txt")

#Leer un archivo
print(mi_archivo.read())


#Mostrar la primera linea
una_linea = mi_archivo.readline()
print(una_linea)

#Mostrara la segunda linea, porque despues de el primer readline se asigna un
#punto al ultimo valor que tomo y el segundo readline parte desde ahi

una_linea = mi_archivo.readline()
print(una_linea)


#Mustra la tercera linea
una_linea = mi_archivo.readline()
print(una_linea)

#Toma todas las lineas del archivo y las guarda como una lista
todas = mi_archivo.readlines()
print(todas)


#Importante siempre cerrar los archivos despues de usar
mi_archivo.close()

#Ejercicio 1
mi_archivo = open("texto.txt", "r")
print(mi_archivo.read())
mi_archivo.close()

#Ejercicio 2
mi_archivo = open("texto.txt", "r")

una_linea = mi_archivo.readline()

print(una_linea)

mi_archivo.close()

#Ejercicio 3
mi_archivo = open("texto.txt", "r")

una_linea = mi_archivo.readline()
una_linea = mi_archivo.readline()
print(una_linea)