#! /usr/bin/python
import random
x = 0

# Sumar a X un valor aleatorio entre 1 y 5, esto así 10 veces.
for i in range(10):
    x = x + random.randint(1,5)
    print(x)

print(f"\nEl valor total de x es de: {x}")

# Ejercicio 2: Almacenar el número 5 dado un numero aleatorio dentro del rango 1 - 100
print("\n< Iniciando bucle While hasta que y = 5 >")
y = 0
while y != 5:
    y = random.randint(1, 100)
print(y)

""" 
En resumen:
El bucle for permite repetir un numero deseado de veces, mientras
que el While permite repetir algo mientras se cumpla una condicion
de manera indeterminada.
"""