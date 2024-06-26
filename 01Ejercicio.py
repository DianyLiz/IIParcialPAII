# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.

import os
os.system('cls' if os.name == 'nt' else 'clear')

def devolver_distintos(a, b, c):
    suma = a + b + c
    if suma > 15:
        resultado = max(a, b, c)
    elif suma < 10:
        resultado = min(a, b, c)
    else:
        resultado = a + b + c - max(a, b, c) - min(a, b, c)
    return resultado

# Función para ordenar y devolver los valores
def ordena_valores(a, b, c):
    valores = [a, b, c]
    valores.sort()
    return valores

print(devolver_distintos(8, 2, 3))
print(ordena_valores(8, 2, 3))


print(devolver_distintos(8, 2, 3))

# hacer una funcion que retorne esos valores ordenados

# def ordena_valores(a, b, c):
#     valores = [a, b, c]
#     valores.sort()
#     return valores

# print(ordena_valores(8, 2, 3))


