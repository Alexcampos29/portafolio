#Escribe un programa que solicite la edad del usuario y clasifique la edad en una de las siguientes categorías:
#"Infantil" (0-12), "Adolescente" (13-19), "Adulto" (20-59) y "Adulto mayor" (60 o más).
print(" programa#23 clasificacion de  las  edades " )
print ("____________________________ " )
edad =  int(input(" ingrese la edad : ") )
if edad <=0 or edad <= 12 :
    print("infantil")
elif edad <=13 or edad <=19:
    print("adoscente")
elif edad>= 20 or edad <=59:
    print ("adulto")
elif edad >= 60:
    print ("adulto mayor") 
else:
             print(" fuera de rango ")
    