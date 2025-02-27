# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:03:25 2023

@author: Aitor Donado.
"""

from funciones.circulo import area as area
import funciones.circulo as circulo
import os
os.chdir(r"/home/laptop/Formación/Curso Python/SAIATUZ/2 Python/01 Introducción/Teoría")


# Cargarmos un archivo de python creado.
# En ese archivo hemos definido las funciones que necesitamos.
# Tienen que estar en la misma carpeta.

print(circulo.area(25))
print(circulo.perimetro(35))


area(4)

"""
# Otra forma de posibilitar la importación es introducir la ubicación en el path
import sys
sys.path.append('/Users/tu_usuario/proyecto/funciones')

import circulo

print(circulo.area(25))
print(circulo.perimetro(35))

"""
#############################
# Leer un archivo de texto. #
#############################
# Observar los modos de apertura
'''
"r" - Lectura - Valor predeterminado. Abre un archivo para lectura, error si el archivo no existe
"a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
"w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
"x" - Create - Crea el archivo especificado, devuelve un error si el archivo existe
'''

fichero = open("datos/quijote.txt", encoding="utf8")
# Contenido como string
libro = fichero.read()
lineas = fichero.readlines()
fichero.close()

libro.count("Sancho")
libro.count("Quijote")
libro.count("Dulcinea")


print(libro[5000:6000])
libro[5000:6000]

libro = libro.replace("\n", " ")
print(libro[5000:6000])

libro = libro.replace("\n\n", "$$$SaltoRenglon%%%")
libro[5000:6000]
libro = libro.replace("\n", " ")
libro[5000:6000]
libro = libro.replace("$$$SaltoRenglon%%%", "\n\n")
libro[5000:6000]
print(libro[5000:6000])


# Añadir un nombre a un fichero de texto. Si no existe, se crea.
fichero = open("datos/nombres.txt", "w")
fichero.write('Ekaitz' + '\n')
fichero.close()

fichero = open("datos/nombres.txt", "a")
fichero.write('Aitor' + '\n')
fichero.close()

fichero = open("datos/nombres.txt", "r")
lineas = fichero.readlines()
fichero.seek(0)
contenido = fichero.read()
fichero.close()
print(lineas)

# Ventaja de usar una estructura with al abrir un archivo
"""
Se asegura que el archivo se cerrará automáticamente al finalizar el bloque de código 
dentro de la estructura with, incluso si se produce un error o una excepción durante 
la ejecución del código. Esto evita que el archivo quede abierto accidentalmente, 
lo que podría causar problemas de rendimiento o corrupción de datos.
"""

with open('datos/quijote.txt', 'r', encoding="utf8") as archivo:
    contenido = archivo.read()

print(contenido[:300])

# Usando el puntero
with open('datos/nombres.txt', 'r', encoding="utf8") as archivo:
    archivo.seek(2)   # Puntero al principio
    contenido2 = archivo.read(7)

print(contenido2)

#########################
# Lectura con escritura #
#########################

# Se puede abrir un fichero en modo lectura con escritura,
# pero éste debe existir préviamente.
# Además por defecto el puntero estará al principio y si escribimos algo
# sobreescribiremos el contenido actual

# Creamos un fichero de prueba con 4 líneas
fichero = open('datos/fichero2.txt', 'w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('datos/fichero2.txt', 'r+')
fichero.write("0123456789")
fichero.close()

with open('datos/fichero2.txt', 'r', encoding="utf8") as archivo:
    print(archivo.read())


# Volvemos a poner el puntero al inicio y leemos hasta el final
fichero.seek(0)
print(fichero.read())
fichero.close()

#########################
# Modificar una línea  #
# "
"""
Para lograr este fin lo mejor es 
    leer todas las líneas en una lista, 
    modificar la línea en la lista, 
    posicionar el puntero al principio y 
    reescribir de nuevo todas las líneas:
"""

fichero = open('datos/fichero2.txt', 'r+')
texto = fichero.readlines()

# Modificamos la línea que queramos a partir del índice
texto[2] = "Esta es la línea 3 modificada\n"

# Volvemos a poner el puntero al inicio y reescribimos
fichero.seek(0)
fichero.writelines(texto)
fichero.close()

# Leemos el fichero de nuevo
with open("datos/fichero2.txt", "r") as fichero:
    print(fichero.read())
