# 9.	Una tienda de música ha puesto a la venta DVD 
# de diversos géneros con los precios que se describe en la siguiente tabla:



salsa = 56
rock = 63
pop = 87
folclore = 120.5
compra = input("¿Qué disco desea comprar? (folclore, salsa ,rock, pop,): ")
cantidad = int(input("¿Cuántos discos desea comprar? "))
if compra == "salsa":
    if 1 <= cantidad <= 3:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*salsa,"\nDescuento: Ninguno","\nNuevo precio a pagar:S/",cantidad*salsa)
    elif cantidad == 4:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*salsa,"\nDescuento: 6% equivalente a S/",(((cantidad*salsa)*4)/100),"\nNuevo precio a pagar: S/",(cantidad*salsa)-(((cantidad*salsa)*4)/100))
    elif 5<=cantidad<=10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*salsa,"\nDescuento: 8% equivalente a S/",(((cantidad*salsa)*8)/100),"\nNuevo precio a pagar: S/",(cantidad*salsa)-(((cantidad*salsa)*8)/100))
    elif cantidad > 10:

# Cantidad Porcentaje de descuento
# 1 a 3 No hay descuento
# 4 6.0%
# 5 a 10 8.0%
# Más de 10 10.2%

        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*salsa,"\nDescuento: 10.2% equivalente a S/",(((cantidad*salsa)*10.2)/100),"\nNuevo precio a pagar: S/",(cantidad*salsa)-(((cantidad*salsa)*10.2)/100))
    elif compra == "pop":
     if 1 <= cantidad <= 3:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*pop,"\nDescuento: Ninguno","\nNuevo precio a pagar: S/",cantidad*pop)
    elif cantidad == 4:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*pop,"\nDescuento: 6% equivalente a S/",(((cantidad*pop)*4)/100),"\nNuevo precio a pagar: S/",(cantidad*pop)-(((cantidad*pop)*4)/100))
    elif 5<=cantidad<=6:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*pop,"\nDescuento: 8% equivalente a S/",(((cantidad*pop)*8)/100),"\nNuevo precio a pagar: S/",(cantidad*pop)-(((cantidad*pop)*8)/100))
    elif 6<cantidad<=10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nObsequio: Póster","\nPrecio: S/",cantidad*pop,"\nDescuento: 8% equivalente a S/",(((cantidad*pop)*8)/100),"\nNuevo precio a pagar: S/",(cantidad*pop)-(((cantidad*pop)*8)/100))
    elif cantidad > 10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nObsequio: Póster","\nPrecio: S/",cantidad*pop,"\nDescuento: 10.2% equivalente a S/",(((cantidad*pop)*10.2)/100),"\nNuevo precio a pagar: S/",(cantidad*pop)-(((cantidad*pop)*10.2)/100))
    elif compra == "rock":
     if 1 <= cantidad <= 3:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*rock,"\nDescuento: Ninguno","\nNuevo precio a pagar: S/",cantidad*rock)
    elif cantidad == 4:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*rock,"\nDescuento: 6% equivalente a S/",(((cantidad*rock)*4)/100),"\nNuevo precio a pagar: S/",(cantidad*rock)-(((cantidad*rock)*4)/100))
    elif 5<=cantidad<=6:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*rock,"\nDescuento: 8% equivalente a S/",(((cantidad*rock)*8)/100),"\nNuevo precio a pagar: S/",(cantidad*rock)-(((cantidad*rock)*8)/100))
    elif 6<cantidad<=10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nObsequio: Póster","\nPrecio: S/",cantidad*rock,"\nDescuento: 8% equivalente a S/",(((cantidad*rock)*8)/100),"\nNuevo precio a pagar: S/",(cantidad*rock)-(((cantidad*pop)*8)/100))
    elif cantidad > 10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nObsequio: Póster","\nPrecio: S/",cantidad*rock,"\nDescuento: 10.2% equivalente a S/",(((cantidad*rock)*10.2)/100),"\nNuevo precio a pagar: S/",(cantidad*rock)-(((cantidad*pop)*10.2)/100))
    elif compra == "folclore":
     if 1 <= cantidad <= 3:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*folclore,"\nDescuento: Ninguno","\nNuevo precio a pagar: S/",cantidad*folclore)
    elif cantidad == 4:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*folclore,"\nDescuento: 6% equivalente a S/",(((cantidad*folclore)*4)/100),"\nNuevo precio a pagar: S/",(cantidad*folclore)-(((cantidad*folclore)*4)/100))
    elif 5<=cantidad<=10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*folclore,"\nDescuento: 8% equivalente a S/",(((cantidad*folclore)*8)/100),"\nNuevo precio a pagar: S/",(cantidad*folclore)-(((cantidad*folclore)*8)/100))
    elif cantidad > 10:
        print("Compra: ", compra,"\nCantidad: ",cantidad,"\nPrecio: S/",cantidad*folclore,"\nDescuento: 10.2% equivalente a S/",(((cantidad*folclore)*10.2)/100),"\nNuevo precio a pagar: S/",(cantidad*folclore)-(((cantidad*folclore)*10.2)/100))
    else:
        print("Ese disco no existe.")
        print("\nGracias por su compra.")