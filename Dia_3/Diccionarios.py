#Diccionarios

#Clave y valor
#no se puede buscar mediante un index
#Util para guardar datos de un objeto
#Claves unicas, pero valores pueden ser iguales
diccionario = {"c1": "valor1", "c2": "valor1"}
print(diccionario)
print(type(diccionario))

resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre":"Sebastian", "apellido": "Jeldres", "peso":95, "talla":175}
print(cliente)

#Buscar por clave
consulta = cliente["apellido"]
print(consulta)

dic = {"c1":55, "c2":[10,20,30], "c3":{"s1":100, "s2":55}}
print(dic["c2"][1])
print(dic["c3"]["s1"])

dic1 = {"c1":["a", "b","c"], "c2":["d", "e","f"]}
E = dic1["c2"][1]
print(E.upper())

#Agregar elementos
dic2 = {1: "A", 2: "B", 3: "C"}
print(dic2)

dic2[4] = "D"
print(dic2)

#Sobreescribir
dic2[4] = "E"
print(dic2)


print(dic2.keys())
print(dic2.values())
print(dic2.items())

#Ejercicio 1
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista

mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

#Ejercicio 2
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#Ejercico 3
mi_dic4 = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic4["edad"] = 36
mi_dic4["ocupacion"] = "Editora"
mi_dic4["pais"] = "Colombia"

print(mi_dic4)