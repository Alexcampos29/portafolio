# Escribe un programa que solicite la edad del usuario y determine el tipo de licencia de
# conducir que puede obtener: "Licencia de menor" (16-17 años), "Licencia de adulto"
# (18-65 años) y "Licencia de adulto mayor" (más de 65 años). 
print("programa#34 Determinar el tipo de licencia de conducir:")
print("_______________________________________\n")
edad = int(input("Ingrese su edad: "))

if edad >= 16 and edad <= 17:
    licencia = "Licencia de menor"
if edad >= 18 and edad <= 65:
    licencia = "Licencia de adulto"
else:
    licencia = "Licencia de adulto mayor"

print(f"aplica para: {licencia}")