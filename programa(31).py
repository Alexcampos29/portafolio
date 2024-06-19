#Escribe un programa que solicite las longitudes de los tres lados de un triángulo
# determine si es un triángulo válido (la suma de las longitudes de dos lados debe ser mayor que la longitud del tercer lado)
print(" programa#31 etermine si es un triángulo válido ")
lado1 = float(input("digite el primer lado: " ))
lado2 = float(input( " digite el segundo lado: " ))
lado3 = float(input( " digite  el tercer lado:  "))

if ((lado1 + lado2) > lado3) or ((lado1 + lado3) > lado2) or ((lado2 + lado3) > lado1):
    print("Los lados ingresados forman un triángulo válido.")
else:
    print("Los lados ingresados no forman un triángulo válido.")
    