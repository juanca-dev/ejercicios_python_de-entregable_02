# 2.	Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
# Obtener el porcentaje que cada uno invierte con respecto
#  a la cantidad total invertida.

print("Ingresamos las cantidades montos invertidos:")
A=int(input("Inversionista A: $."))
B=int(input("Inversionista B: $."))
C=int(input("Inversionista C: $."))
D=(A+B+C)

print('Porcentaje  invertido del inversionista en "A" es:',(A*100)/D,"%")
print('Porcentaje  invertido del inversionista en "B" es:',(B*100)/D,"%")
print('Porcentaje  invertido del inversionista en "C" es:',(C*100)/D,"%")
