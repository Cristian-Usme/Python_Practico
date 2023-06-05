"""Escribir un programa que pregunte al usuario una cantidad a 
invertir, el interés anual y el número de años, y muestre por 
pantalla el capital obtenido en la inversión."""

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese la tasa de interés anual (porcentaje): "))
nro_anhos = int(input("Ingrese la cantidad de años: "))

total_neto = round(cantidad * ((interes / 100 + 1) ** nro_anhos), 2)
ganancias = round(total_neto - cantidad, 2)

print(
    f"El total obtenido en un plazo de {nro_anhos} años, \ncon un interes del {interes}% por año, es de: ${total_neto} \ny unas ganancias de: ${ganancias}")
