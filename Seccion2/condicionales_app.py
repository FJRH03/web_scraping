#! /usr/bin/python
import random 
x = random.randint(1,5)

if x == 1:
    print('Hola soy el numero 1')
elif x == 3:
    print('Hola soy el numero 2')
else:
    print('Hola soy cualquier otro numero.')
print(f"El valor de X es de: {x}")

y = 4
# or/and 
print("\n<Or y and>")
print(x >= 5 and y == 4) # True