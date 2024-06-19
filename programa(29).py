#Escribe un programa que solicite al usuario su salario bruto
#y calcule el salario neto después de aplicar un impuesto del 20% si el salario bruto es mayor a $2000.
print(" programa#29 calcular el salario neto ")
salario = float(input( "  ingrese  el salario bruto: " ))
if salario >  2000:
    imp = salario * 0.20
    sal_brut = salario - imp
    print (" tiene impuesto " )
else:
    sal_brut = salario
    print( " el salario neto  no tiene impuesto")
                
