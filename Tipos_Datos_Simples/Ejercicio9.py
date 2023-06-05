"""Imagina que acabas de abrir una nueva cuenta de ahorros que te 
ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience 
leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y
mostrar por pantalla la cantidad de ahorros tras el primer,
segundo y tercer años. Redondear cada cantidad a dos decimales."""

cant_ini = float(input("Ingrese la cantidad de dinero inicial: "))
percent = 0.04
anho1 = round((cant_ini * percent) + cant_ini, 2)
anho2 = round((anho1 * percent) + anho1, 2)
anho3 = round((anho2 * percent) + anho2, 2)

print(
    f"La cantidad de ahorros tras el primer año es de: ${anho1}\nTras el segundo: ${anho2}\nTras el tercero: ${anho3}")
