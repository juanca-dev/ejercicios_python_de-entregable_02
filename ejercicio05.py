# 5.Diseñe un algoritmo que lea tres números y determine el número mayor.
a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

if(a > b and a > c):
    print("El número mayor es",a)
else:
  if(b > a and b > c):
     print("El número mayor es",b)
  else:
      print("El número mayor es",c)