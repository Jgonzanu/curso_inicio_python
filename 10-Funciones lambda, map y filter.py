#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:51:51 2023

@author: laptop
"""

#######################
# List comprehension  #
#######################
import random


def divide2(num):
    print(f"Divido {num} entre 2")
    return num/2


lista_num = [divide2(elemento) for elemento in range(0, 300, 15)]

# Desordenamos la lista de manera aleatoria
random.shuffle(lista_num)

########
# Map  #
########

# map aplica una función cualquiera a un iterable


def duplica(numero):
    return 2 * numero


lista_num2 = list(map(duplica, lista_num))

iterable = map(duplica, lista_num)

next(iterable)
next(iterable)
next(iterable)
next(iterable)
next(iterable)
next(iterable)
next(iterable)


def imprime(numero):
    return f"Este término está ocupado por el elemento {str(numero)}"


iterable = map(imprime, lista_num)
next(iterable)
next(iterable)
next(iterable)
next(iterable)
next(iterable)
next(iterable)
next(iterable)

lista_desde_iterable = list(iterable)

###########
# Filter  #
###########
# filter, es un map usando una función que devuelve True o False


def tiene_decimales(num):
    if num == int(num):
        return False
    else:
        return True


iterable_num_decimales = filter(tiene_decimales, lista_num)
lista_num_decimales = list(iterable_num_decimales)


###########
# Lambda  #
###########
# Lambda por reducción de una función sencilla
iterable2 = map(lambda x: x * 2, lista_num)

next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)

iterable3 = map(lambda x, y: x + y, lista_num, lista_num2)
lista_num3 = list(iterable3)


#___________#
# Ejercicio #
#-----------#

# Crear una lista con los números de 0 al 100.
lista100 = list(range(0, 101))

# Dividirlos entre tres con map y una función lambda.
listatercios = list(map(lambda x: x/3, lista100))

# Filtrar los que tienen parte decimal con una función lambda.


def tiene_decimales(num):
    if num == int(num):
        return False
    else:
        return True


def tiene_decimales(num):
    return num != int(num)


lista_tercios_decimales = list(filter(lambda x: x != int(x), listatercios))

#__________#
# Solución #
#----------#


edades = [random.randint(-7, 130) for i in range(500)]
edades.count(-3)
edades.count(121)


# Usar filter para eliminar los valores

def es_correcto(edad):
    return edad >= 0 and edad <= 120


edades_correctas = list(filter(lambda x: x >= 0 and x <= 120, edades))
edades_correctas.count(121)

# Usar map para sustituirlos por 120 o 0


def corrector(edad):
    if edad > 120:
        return 120
    elif edad < 0:
        return 0
    else:
        return edad


edades_correctas2 = list(map(corrector, edades))
edades_correctas2.count(-3)
