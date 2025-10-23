edad = int(input("Introduce tu edad: "))
if edad < 4:
        precio = 0
elif edad <= 18:
        precio = 4
else:
        precio = 10000
        print("El precio de la entrada es", "$", precio)
