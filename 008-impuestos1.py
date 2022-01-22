IMPUESTO = 0.21
num1 = float(input("Introduce primer número:"))
num2 = float(input("Introduce segundo número:"))
impuesto = float(input("Dime el porcentaje de IVA:")/100)
if impuesto==0:
    impuesto=IMPUESTO
print("IMPORTE FACTURA=",num1+num2+(num1+num2)*impuesto)