#determinar si una persona es adolescente
#escribe un programa que solicite la edad del usuario y determine si es un adolescente
#(entre13 y 19 años)
print( "programa#1 determinar si una persona es adolescente: " )
print( "_____________________________________" )
edad= int(input(" digite una edad: "))
if edad <13:
    print("no es adolescente")
elif edad >= 13  and edad  <= 19:
    print (" es adolescente")
else:
    print("es mayor de edad")
    