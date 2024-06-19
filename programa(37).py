#Escribe un programa que solicite la distancia recorrida en kilómetros y calcule la tarifa
# del taxi. La tarifa es $2.50 por kilómetro para los primeros 10 kilómetros y $2.00 por kilómetro adicional. 
print("programa# 37 calcular la tarifa de un taxi")
print("--------------------------------------------\n")
km = float(input ( " ingrese los kilometros: "))
if  km <=  10:
    tarifa = km *  2.50
else:
    tarifa= 10 * 2.50 +( km -10) *2.00
print(f"La tarifa del taxi es: ${tarifa:.2f}")