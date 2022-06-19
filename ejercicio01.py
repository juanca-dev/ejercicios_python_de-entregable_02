# 1.Escribe un programa que solicité al usuario ingresar cuatro números para luego mostrar 
# el promedio de los cuatro.

print("Ingrese 4 números para mostrar el promedio de los 4 números:")
n1 = float(input("first number"))
n2 = float(input("second number"))
n3 = float(input("third number"))
n4 = float(input("fourth number"))

multiplcamos = (n1+n2+n3+n4)/4

print("El promedio de los cuatro  numeros es",round(multiplcamos,2))