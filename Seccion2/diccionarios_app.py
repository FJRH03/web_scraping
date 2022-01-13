#! /usr/bin/python

# Los diccionarios permiten acceder a los valores a traves de las claves
d = {
    "nombre": "Francisco",
    "edad": 25
}

print(d["edad"])

# Agregar elementos al diccionario
d["apellido"] = "Ramirez"
print(d)

# Eliminar elementos de un diccionario
del d["edad"]
print(d)

d["edad"] = 15

# Iterar un diccionario
for k, v in list(d.items()):
    print(k, v)

# Anidar diccionarios
print("\n")
d2 ={
    "nombre": "Javier",
    "edades": {
        "edad papa": 48,
        "edad mama": 45,
        "edad hijo": 23
    }
}

print(d2["edades"]["edad papa"])