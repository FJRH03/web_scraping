#! /usr/bin/python
numeros = [9, 6, 1, 3, 5]
print(numeros[0]) # indexacion
print(numeros[-1]) #Indexacion inversa

# Metodos usados para manejar las listas
numeros.append(4) # agregar 4 a la lista de elementos
numeros.remove(3) # eliminar la primera aparicion de 6
numeros.pop(1) # Elimina el elemento con el index 1

numeros[0] = 10 # Agregando un cero en la posicion 0
print(numeros)
len(numeros)

# Imprime True si existe 10 en la lista numeros
print("\nExiste el numero 10 en la lista:")
print (10 in numeros)

# Ordenar una lista en orden ascendente
print("\nOrdenar elementos de manera ascendente ->")
numeros.sort()
print(numeros)

# Ordenar los numeros de manera descendente
print("\nOrdenar elementos de manera descendente ->")
numeros.reverse()
print(numeros)

# Recorrer una coleccion
print("\nIterar elementos de la lista numeros -> ")
for i in numeros:
    print(i)

print("\nRecorriedo caracteres de una cadena ->")
# Cadenas de Texto pueden ser vistas como una lista de caracteres
cadena = "Hola mundo"

for c in cadena:
    print(c)

print(cadena.capitalize())
print(cadena.startswith("H")) #true
print(cadena.endswith("mundo")) #true
print(cadena.isalnum())


#Eliminar espacios al inicio y al final del texto
#print(cadena.strip())

print("\nFuncion split y funcion join ->")
# Funcion split y funcion join
frutas = "Duraznos, Manzanas, Papaya"
print("Cadena original: " + frutas)
print(frutas.split(","))

# Pasamos una lista a una cadena (String)
frutas2 = frutas.split(",")
print(frutas2)
cadena2 = " -".join(frutas2)
print("La nueva cadena es: " + cadena2)