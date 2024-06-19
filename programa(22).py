# Escribe un programa que solicite una palabra al usuario
#y determine si  tiene mas de 5 letras
print(" Verificar si una palabra tiene mas de 5 letras: " )
print( "  _____________________________________ " )
palabra = input(" escriba una palabra: " )
if len(palabra) > 5:
    print("La palabra tiene más de 5 letras.")
else:
    print("La palabra tiene menos de 5 letras.")