"""Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y la empresa de 
logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete
a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir 
un programa que lea el número de payasos y muñecas vendidos en el 
último pedido y calcule el peso total del paquete que será enviado."""

peso_payasos = 112
peso_munhecas = 75

cant_munhecas = int(input("Cuántas muñecas fueron vendidas: "))
cant_payasos = int(input("Cuántos payasos fueron vendidos: "))

peso_total = (cant_munhecas * peso_munhecas)+(cant_payasos * peso_payasos)

print(f"El peso total del paquete que será enviado es: {peso_total}")
