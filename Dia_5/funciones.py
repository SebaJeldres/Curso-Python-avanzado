#Bloque de codigo reutilizable
#funciones != metodos
#Las creamos nosotros
#Se inicia con un def
#Se recomienda añadir una descripcion


def saludar_persona(nombre):
    '''
    Este funcion sive para saludar a las personas
    '''
    print("Hola")


nombre = input("Ingresa tu nombre: ")
saludar_persona(nombre)


#Ejercicio 1
def saludar():
    print("¡Hola mundo!")

#Ejercicio 2

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")


nombre_persona = "Sebastian"

#Ejercicio 3
def cuadrado(un_numero):
    print(un_numero ** 2)


un_numero = 43