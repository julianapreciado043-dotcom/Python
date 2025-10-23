print("Bienvenido a la pizzeria Bella Napoli\nTipos de pizza\n\t1- Vegeteriana\n\t2- No vegeteriana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")

if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("Pimiento")
    else:
        print("Tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
ingrediente = input("Introduce el ingrediente que deseas: ")
print("Pizza no vegetariana con mozzarella, tomate y ", end="")
if ingrediente == "1":
    print("Peperoni")
elif ingrediente == "2":
    print("Jamón")
else:
    print("Salmón")