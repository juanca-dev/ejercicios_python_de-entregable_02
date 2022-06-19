# 7.	Elabore un algoritmo que permita calcular el área de un triángulo.
# Área = (base * altura) /2
altura =int(input("Ingrese la altura del triangulo: "))
base =int(input("Ingrese la base del triangulo: "))
def Area_Triangulo():
    area = (base*altura)/2
    return area
print(Area_Triangulo())   
