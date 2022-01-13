#! /usr/bin/python

# Las tuplas una vez definidas no se pueden modificar (inmutables)
mi_tupla = (1,6,7)
print(mi_tupla)
# mi_tupla[0] = 9 -> 'tuple' object does not support item assignment

# Convertir una lista a tupla
mi_lista = [1,3,4,6]
print(type(mi_lista))
nueva_tupla = tuple(mi_lista)
print(type(nueva_tupla))