# 8.	Diseñe un algoritmo que verifique si la cantidad de dígitos ingresados de un DNI
#  es correcta o no (el DNI tiene 8 dígitos).

numero_DNI=input("Ingrese su numero de DNI:")
codigo = len(numero_DNI)
if codigo > 8:
    print("El número de  DNI es incorrecto digite correctamente los 8 digitos")
elif codigo < 8:
    print("El número de  DNI es incorrecto digite correctamente los 8 digitos")
else:
    print("El número de  DNI es correcto")        