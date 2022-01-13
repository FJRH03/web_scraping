#! /usr/bin/python
f = open("archivo.txt", "r")
# print(f.readlines())  -> leer todo el archivo

# Leer un archivo linea por linea (iterar archivo)
for line in f:
    line = line.strip() # limpieza de los caracteres no deseados
    line = line.split(',')
    print(line[0])

f.close()

# Agregar una linea al archivo
f = open("archivo.txt", "a")
f.write("\nManzana,1,10")

# Crear un archivo
f = open("archivo2.txt", "w")
f.write("Hola Mundo!")