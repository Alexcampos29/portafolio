#Escribe un programa que solicite un nombre al usuario y determine si el nombre es
#corto (menos de 5 letras), mediano (5-8 letras) o largo (más de 8 letras). 
print(". programa#36 Verificar si un nombre es corto, mediano o largo:")
print("_____________________________________________\n")
nombre = input("Ingrese su nombre: ")

largo_nombre = len(nombre)

if largo_nombre < 5:
    print(f"El nombre {nombre} es corto.")
elif largo_nombre <= 8:
    print(f"El nombre {nombre} es mediano.")
else:
    print(f"El nombre {nombre} es largo.")
