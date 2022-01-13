#! /usr/bin/python
def suma(lista):
    x = 0
    for n in lista:
        x += n
    return x

sumatoria  = suma([1,2,3,4,5])
print(sumatoria)