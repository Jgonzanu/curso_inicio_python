# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:03:25 2023

@author: Aitor Donado
"""

################
# RECURSIVIDAD #
################

"""
Las funciones recursivas en Python tienen varias ventajas, entre las que se incluyen:

1. Claridad de código: Las funciones recursivas pueden hacer que el código sea 
    más fácil de leer y entender, especialmente para problemas que implican una 
    estructura de árbol o una división en subproblemas más pequeños. 
    En algunos casos, el uso de funciones recursivas puede ser más sencillo y más 
    claro que el uso de bucles iterativos.

2. Eficiencia en la programación de algoritmos complejos: 
    Las funciones recursivas son especialmente útiles para problemas que 
    implican la división en subproblemas más pequeños, como los algoritmos de 
    búsqueda y ordenación. Estos algoritmos pueden ser difíciles de implementar 
    de forma iterativa, pero se pueden escribir de manera más sencilla y 
    eficiente mediante funciones recursivas.

3. Ahorro de espacio de memoria: En algunos casos, las funciones recursivas 
    pueden ahorrar espacio de memoria, ya que pueden evitar la necesidad de 
    almacenar datos en estructuras de datos temporales.

4. Mayor flexibilidad: Las funciones recursivas pueden ser utilizadas en 
    una amplia variedad de situaciones, lo que las hace más flexibles que las 
    funciones iterativas.

Sin embargo, es importante tener en cuenta que las funciones recursivas también 
pueden tener algunas desventajas, como la sobrecarga de la pila de llamadas y 
la posibilidad de causar un bucle infinito si no se implementan correctamente. 
Es importante diseñar y probar cuidadosamente las funciones recursivas antes 
de utilizarlas en proyectos importantes.
"""

# Cálculo de un número factorial con recursividad:
    
def factorial(n):
    # Caso base: Si n es 0 o 1, el factorial es 1.
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: El factorial de n es n multiplicado por el factorial de n-1.
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
resultado = factorial(5)
print("El factorial de 5 es:", resultado)

# Función que mediante recursividad multiplique todos los valores de una lista.
def mult_list_recur(lista):
    # Caso base
    if len(lista) == 1:
        print("Y por último multiplico por", lista[0])
        return lista[0]
    # Caso recursivo
    else:
        print("Estoy multiplicando por", lista[0])
        return lista[0]*mult_list_recur(lista[1:])


print(mult_list_recur([1, 3, 5, 7, 9]))

print(mult_list_recur([1, 3, 0, 7, 9]))

print(mult_list_recur([1, 7, 1, 1, 9]))

print(mult_list_recur([1, 1, 1, 7, 9]))


# Sin recursividad usaríamos una iteración
def mult_list(lista):
    salida = 1
    for elemento in lista:
        salida = salida * elemento
    return salida


print(mult_list([1, 3, 5, 7, 9]))

print(mult_list([1, 3, 0, 7, 9]))

print(mult_list([1, 7, 1, 1, 9]))

print(mult_list([1, 1, 1, 7, 9]))

# Función que calcula la serie de Fibonacci
# donde Fn = F(n-1)+F(n-2)
#       F0 = 0
#       F1 = 1
# 0,1,1,2,3,5,8,13,21,34,55,89,...

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

fib_recur(9)

# Mismo ejemplo resuelto de manera iterativa
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

fib_iter(9)

# Función que calcule de manera recursiva la multiplicación de un número 'n' 
# por 3, mediante la suma recursiva de 3 'n' veces, sin utilizar multiplicaciones
# Tenemos que definir primero el caso base:
# f(0) = 3
# f(1) = f(0) + 3 = 3 + 3
# f(2) = f(1) + f(0)
# ...
# f(n) = f(n-1)+f(n-2)

def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

mult3(15)


def mult4(n):
    if n == 1:
        return 4
    else:
        return mult4(n-1) + 4

mult4(5)
