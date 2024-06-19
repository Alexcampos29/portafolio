#o Escribe un programa que solicite un número al usuario y determine si es divisible por 3,
#por 5, por ambos o por ninguno.
print("programa#35 Determinar si un número es divisible por 3 y 5:")
numero = float(input(" escriba un numero: "))
if numero %3 ==0 and numero %5 == 0:
    print(" es divisible por ambos")
elif numero%3==0:
    print(" es divisible por 3 ")
elif numero %5 == 0:
    print (" es divisible por 5")
else:
    print(" no es divisible por 3 ni por 5")