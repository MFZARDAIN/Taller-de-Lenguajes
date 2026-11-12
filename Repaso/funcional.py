# Funciones lambda
# --Función anónima (sin nombre)
# --Se usa para abreviar
# --Nunca tendrá condicionales ni bucles
area = lambda b, h : (b * h) / 2
print("Resultado Area: ", area(6, 9))

# Funciones de orden superior
# -- Funciones pueden pasarse como argumentos de una función
def aplica(f, arg):
    return f(arg)

def cuadrado(n):
    return n * n

def cubo(n):
    return n**3

def exponente(arg):
   n = arg[0]
   m = arg[1]
   return n**m

print("Resultado Función Aplica: ", aplica(cuadrado, 9))
print("Resultado Función Aplica: ", aplica(cubo, 3))
print("Resultado Función Aplica: ", aplica(exponente, [2, 9]))

# filter
# -- Verifica que los elementos de una secuencia cumplen una condición, devolviendo un iterador con los elementos que cumple dicha condición
def par(n):
  return n % 2 == 0

def impar(n):
  return n % 2 == 1

print("Resultado Función Filter: ", list(filter(par, [54, 21, 77, 40, 2, 0, 90, 99, 1])))

# map
# -- Aplica una función a cada elemento de una lista iterable (listas, tuplas, etc.) devolviendo una lista con los resultados
def cuadrado(n):
    return n * n
print("Resultado Función Map: ", list(map(cuadrado, [2, 2, 2, 2, 2, 10])))

# reduce
# -- Operar todos elementos de una colección iterable (reduce)
# -- reduce(f, l): aplicar la función f a los dos primeros elementos de la secuencia l
# -- Con ese valor vuelve aplicar con el siguiente
from functools import reduce

def producto(n, m):
    return n * m
print("Resultado Función Reduce: ", reduce(producto, [2, 2, 2, 2, 2, 10]))

#Test1

from collections import Counter

correos = ['a@mecon.gob.ar', 'b@mecon.gob.ar', 'c@afip.gob.ar', 'd@mecon.gob.ar']

dominios = list(map(lambda correo: correo.split('@')[1], correos))

conteo = Counter(dominios)

for dominio, cantidad in conteo.items():
    print(f"{dominio}: {cantidad}")

#Test 2

def primo(n):
  cont=0
  if n == 1 or n == 0:
     return False
  for i in range (1, n):
    if n % i == 0:
       cont += 1
  return cont <= 2

print("Resultado Función Primo: ", list(filter(primo, [83, 13, 77, 41, 2, 0, 90, 7, 1])))