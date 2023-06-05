"""Escribir un programa que lea un entero positivo, n, introducido
por el usuario y después muestre en pantalla la suma 
de todos los enteros desde 1 hasta n. La suma de los n primeros
enteros positivos puede ser calculada de la siguiente forma:
https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
revisar el ejercicio 6"""

n = int(input("Ingrese un número: "))
suma = (n * (n + 1)) / 2

print(suma)
