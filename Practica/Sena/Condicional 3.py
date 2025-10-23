edad=int(input("Introduce tu edad: "))
# Decision del precio en función de la edad
if edad <4:
     precio=0
elif edad <=18:
      precio=4
else:
    precio=10000
    #Mostrar precio
print("El precio de la entrada es ","$",precio)