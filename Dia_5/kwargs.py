#se les puede dar un noombre a los valores indefinidos que se ingresar como parametro en la funcion


def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(clave, valor)
        total += valor
    return total


print(suma(x=3, y=5, z=2))



def prueba(num1, num2, *args, **kwargs):
    print(num1, num2)

    for arg in args:
        print(arg)

    for clave,valor in kwargs.items():
        print(clave, valor)


prueba(12,33,45,545,45345,5435,232, x=3, y=3, z=4)

#Ejercicio 1
def cantidad_atributos(**kwargs):
    conteo = 0

    for n in kwargs:
        conteo += 1

    return conteo

#Ejercicio 2
def lista_atributos(**kwargs):
    return list(kwargs.values())


#Ejercicio 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_arg, valor in kwargs.items():
        print(f"{nombre_arg}: {valor}")
