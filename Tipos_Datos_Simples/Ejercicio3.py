"""Escribir un programa que pregunte al usuario por el número 
de horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde."""

cant_horas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = int(input("Ingrese el valor de cada hora: "))

print(f"Su paga es de: ${cant_horas * valor_hora}")
