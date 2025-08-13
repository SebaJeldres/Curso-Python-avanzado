nombre = input("Ingrese su nombre")
venta = int(input("Ingrese su venta"))

comision = venta * 13 / 100

comision = round(comision, 2)

print(f"Hola {nombre}, su comision es {comision}")