# open tiene otro argumento
# "r": Solo lectura
# "w": solo escritura | si el archivo viene con contrenido, lo borra y añade el que se escriba desde el codigo
# "a": solo escritura al final del archivo | Util para dejar registro en un bloc de notas, ejemplo en el caso de querer registrar los avances diarios


archivo = open("prueba.txt", "w")

archivo.write("Soy el nuevo texto") #No agrega un salto de linea

archivo.writelines(["hola", "mundo", "aqui", "estoy"]) #escribe los arguementos juntos

#Asi escribe la lista con salto de linea
lista = ["hola", "mundo", "aqui", "estoy"]

for i in lista:
    archivo.write(i + "\n")


archivo.close()

#Ejercicio 1
mi_archivo = open("mi_archivo.txt", "w")

mi_archivo.write("Nuevo texto")

mi_archivo.close()

mi_archivo = open("mi_archivo.txt", "r")

print(mi_archivo.read())


#Ejercicio 2
mi_archivo = open("mi_archivo.txt", "a")
mi_archivo.write("Nuevo inicio de sesión")
mi_archivo.close()

mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())

#Ejercicio 3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

mi_archivo = open("registro.txt", "a")

for p in registro_ultima_sesion:
    mi_archivo.write(p + "\t")

mi_archivo.close()

mi_archivo = open("registro.txt", "r")
print(mi_archivo.read())