#Escribe un programa que solicite al usuario los años de experiencia y determine la
#categoría del trabajador: "Junior" (menos de 2 años), "Semi-Senior" (2-5 años), "Senior"(más de 5 años). 
print("programa #32 Determinar la categoría de un trabajador: " )
Años=float(input("Ingrese los años de experiencia: "))

if Años <= 2:
    print("Junior")

if Años > 2 and Años <= 5:
    print("Semi-Senior")

if Años > 5:
    print("Senior")