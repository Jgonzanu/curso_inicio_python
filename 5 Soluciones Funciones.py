#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:49:00 2023

@author: laptop
"""

# Crear una función que divida un número por tres.
def divide_3(num):
    salida = num/3
    return salida

tercio = divide_3(23)

# Crear una función que eleve a la 10 un determinado valor.
def a_la_10(num):
    salida = num**10
    return salida

a_la_10(2)

from math import pi
pi


# Crear una función que calcule el área de un círculo.
def area_circ(radio):
    area = radio*radio*pi
    return area

area_circ(4)

# Crear una función que calcule el área de un triángulo.
def area_triangulo(base, altura):
    area = base*altura/2
    return area

area_triangulo(base=3, altura=4)
area_triangulo(3, 4)
area_triangulo(altura=4,base=3)

# Crear una función que determine si un número es impar.
def es_impar(num):
    resultado = (num % 2 != 0)
    return resultado

if es_impar(13):
    print("Es Impar")

# Crear una función que encuentre el primer divisor de un número entero
def primer_divisor(num):
    if num % 2 == 0:
        return "Es divisible entre 2"
    elif num % 3 == 0:
        return "Es divisible entre 3"
    elif num % 5 == 0:
        return "Es divisible entre 5"
    else:
        return "No he encontrado divisor"


primer_divisor(10)

def primer_divisor2(num):
    for i in range(2,num):
        if num % i == 0:
            return i
    return num

primer_divisor2(126)

def factoriza(num):
    factores = []
    while num != primer_divisor2(num):
        factores.append(primer_divisor2(num))
        num = int(num/primer_divisor2(num))
    factores.append(num)
    return factores

factoriza(126*17*255)







