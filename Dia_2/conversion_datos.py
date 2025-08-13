#Implicitas
num1 = 20
num2 = 30.5

print(type(num1))
print(type(num2))

num1 = num1 + num2

print(type(num1))

#Explicitas
num1 = 5.8
print(type(num1))

num2 = int(num1)
print(type(num2))

edad = input("dime tu edad")
edad = int(edad)
nueva_edad = edad + 1
print(nueva_edad)

#Ejercicio 1
num1 = 7.5
num1 = int(num1)

print(type(num1))

#Ejercicio 2
num2 = 10
num2 = float(num2)

print(type(num2))

#Ejercicio 3
num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))

