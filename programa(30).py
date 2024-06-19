# Escribe un programa que solicite un año al usuario
# y determine si es el primer año de un siglo (por ejemplo, 1900, 2000, 2100).
print ("programa#30 Determinar si un año es un siglo: " )
print ("________________________________\n ")
año = int(input("Ingrese un año: "))
if año %  100 == 0 and  año %  400 == 0:
    print(f"{año} es el primer año de un siglo.")
elif año %  100 == 0 and año %  4 !=  0:
    print(f"{año} no es el primer año de un siglo.")
elif año % 100 == 0 and año %  4 == 0 :
    print(f"{año} es el primer año de un siglo.")
else:
    print(f"{año} no es el primer año de un siglo.")