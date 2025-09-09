#inmutables
#ocupan menos espacio
#seguridad de los datos

mi_tuple = (1 , 2 , 3 , 4 , 5, (12,34))

print(mi_tuple)

print(type(mi_tuple))

print(mi_tuple[0])

print(mi_tuple[-1][0])

print(mi_tuple[-1])

mi_tuple = list(mi_tuple)
mi_tuple = tuple(mi_tuple)

#asignar contenido

t = (1, 2, 3)
x,y,z = t
print(x,y,z)

print(len(t))
print(t.count(3))
print(t.index(2))

#Ejercicios

#Ejercicio 1

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2))

#Ejercicio 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista = list(mi_tupla)

#Ejercicio 3
mi_tupla2 = (1, 2, 3, 4)

a,b,c,d = mi_tupla2