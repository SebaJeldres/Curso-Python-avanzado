from random import *

#Pedir nombre
#La maquina escoje un numero del 1 al 100
#Tiene 8 intentos para adivinar

#condicionales
#Si es menor a 1 o mayor a 100 "Numero no permitido"
#Si el numero es menor "Es menor al numero secreto"
#Si el numero es mayor "Es mator al numero secreto"
#Si acierta "Adivinaste el numero secreto!!!!, lo lograste en x intentos"
#Si se acaban los intentos se acaba el juego


nombre = input("Ingresa tu nombre: ")
intentos = 8

numero_secreto = randint(1,100)
intentos -= 1

print(f"¡Hola {nombre}!\nLa máquina ha escogido un número aleatorio del 1 al 100.")
print(f"Tienes 8 intentos para adivinarlo.\n")

while intentos > 0:
    numero_escojido = int(input(f"ingresa un numero"))
    if numero_escojido == numero_secreto:
        print(f"Adivinaste el numero secreto!!!!, lo lograste en {10 - intentos} intentos")

    elif numero_escojido < numero_secreto:
        print(f"El numero ingresado es menor al numero secreto, te quedan {intentos} intentos")
        intentos -= 1

    elif numero_escojido > numero_secreto:
        print("El numero escojido es mayor al numero secreto")
        intentos -= 1

    elif numero_escojido < 1 or numero_escojido > 100:
        print("numero no permitido, intenta de nuevo")

else:
    print("Se acabaron los intentos")