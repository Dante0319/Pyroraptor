valor_dolar = float(input("Valor del dolar hoy: "))
cantidad = float(input("Cantidad a convertir: "))
opcion = input("¿Convertir a (D)olares o (P)esos? ")

if opcion.lower() == 'd':
    print(cantidad / valor_dolar, "Dolares")
else:
    print(cantidad * valor_dolar, "Pesos")

