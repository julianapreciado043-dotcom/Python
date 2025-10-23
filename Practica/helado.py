
print("Bienvenido a la heladería Sweet Cream.")
print("Tipos de helado:")
print("1- Base de agua")
print("2- Base de crema")

tipo = input("Introduce el número correspondiente al tipo de helado que quieres: ")

if tipo == "1":
    print("Sabores de helado con base de agua:")
    print("1- Limón")
    print("2- Fresa")
    print("3- Mango")
    sabor = input("Introduce el número del sabor que deseas: ")

    print("Helado con base de agua sabor a ", end="")
    if sabor == "1":
        print("limón 🍋")
    elif sabor == "2":
        print("fresa 🍓")
    else:
        print("mango 🥭")

else:
    print("Sabores de helado con base de crema:")
    print("1- Vainilla")
    print("2- Chocolate")
    print("3- Galleta")
    sabor = input("Introduce el número del sabor que deseas: ")

    print("Helado con base de crema sabor a ", end="")
    if sabor == "1":
        print("vainilla 🍦")
    elif sabor == "2":
        print("chocolate 🍫")
    else:
        print("galleta 🍪")

print("¡Gracias por tu compra! Disfruta tu helado 😋")