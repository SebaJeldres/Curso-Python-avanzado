#Elementos unicos
#no se pueden incluir listas ni diccionarios
#Requiere de un argumento ), [
#No se puede ni buscar ni añadir elementos
#Elimina las repeticiones

mi_set = set([1,2,3,4,5])
print(mi_set)
print(type(mi_set))


otro_set = {1,2,3,4,5}
print(otro_set)
print(type(otro_set))

print(len(otro_set))
print( 2 in otro_set)

s1 = set([1,2,3,4,5])
s2 = set([1,2,3,4,5])
s3 = s1.union(s2)
print(s3)

s1.add(6)
print(s1)

s1.remove(2)
print(s1)

s1.discard(2)
print(s1)

s1.pop() #Elimina uno aleatorio
print(s1)

s1.clear()
print(s1)


#Ejercicios

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

mi_set_3 = mi_set_1.union(mi_set_2)

#Ejercicio 2

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.pop()

#Ejercicio 3
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add("Damián")

