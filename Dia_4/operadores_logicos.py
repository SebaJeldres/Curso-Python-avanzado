# and = si
# or = o
#not = no

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool1 = 10 == 10 or 23 == 23
print(mi_bool1)

texto = "La cebolla morada"
mi_bool2 = ("morada" in texto) and ("cebolla" in texto)
print(mi_bool2)

mi_bool3 = not "a" == "a"
print(mi_bool3)

#Doble negacion
mi_bool4 = not "a" != "a"
print(mi_bool4)

#Ejercicio 1

num1 = 36
num2 = 72/2
num3 = 48

mi_bool = num1 > num2 and num1 < num3

#Ejercicio 2
num1 = 36
num2 = 72/2
num3 = 48

mi_bool = num1 > num2 or num1 < num3

#Ejercicio 3

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not palabra1 in frase and not palabra2 in frase