#! /usr/bin/python

# Los conjuntos no mantienen orden, no tienen indices
lista = [1,5,7]
conjunto = set(lista)

print(type(conjunto))

conjunto2 = {1, 5 ,9}
conjunto2.add(10)
print(conjunto2)

# Los conjuntos no almacenan numeros repetidos
conjunto2.add(10)
print(conjunto2)

# Remover elementos de un conjunto (9)
conjunto2.remove(9)
print(conjunto2)

# Recorrer los elementos de un conjunto

for elem in conjunto2:
    print((elem))

# Preguntar por la existencia de un elemento dentro de un conjunto
print ( 5 in conjunto2) # True

# Union de conjuntos 
print("\nUnion de conjuntos:")
print(conjunto.union(conjunto2))

# Interseccion de conjuntos -> Elementos que coinciden en ambos conjutos
print("\nInterseccion de conjuntos de conjuntos:")
print(conjunto.intersection(conjunto2))