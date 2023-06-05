"""Una panadería vende barras de pan a 3.49€ cada una. El pan que
no es el día tiene un descuento del 60%. Escribir un programa que
comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una
barra de pan, el descuento que se le hace por no ser fresca y el 
coste final total."""

other_day = int(
    input("Ingrese la cantidad de barras vendidas que no son del día: "))
precio = 3.49
precio_descuento = 3.49 * 0.6
descuento = 3.49 - precio_descuento

print(
    f"El descuento es de: 60%\nEl coste final es de: €{round(descuento * other_day, 2)}")
