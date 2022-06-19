# 4.	Ingresar 2 números y luego escoger la operación que se quiere hacer con ellos (suma, resta, multiplicación o división) 
# y reportar el resultado.

num1 = int(input("Ingrese un número: "));
num2 = int(input("Ingrese otro número: "));
operacion = input("suma, resta, division, multiplicación:  ")

if operacion == "suma":
    print(num1 + num2)
elif operacion == "resta":
    print(num1 - num2)
elif operacion == "división":
    print(num1 / num2)
elif operacion == "multiplicación":
    print(num1 * num2)    
