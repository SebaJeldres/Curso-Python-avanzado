#Documentacion de python

dic = {"clave1":100, "clave2":500}

a= dic.popitem()

print(a)
print(dic)


#Ejercicio 1
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:_#,,,,,,:::____##')

print(texto)

#Ejercicio 2
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, "naranja")
#Ejercicio 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)