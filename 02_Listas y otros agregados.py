#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:43:39 2023

@author: laptop
"""
#########################
# TRABAJANDO CON LISTAS #
#########################


# Lista de texto.
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

# Lista numerica.
enteros = [1, 2, 3, 4, 5, 7]

type(enteros[0])


# lista mixta
lista_mixta = ["Lunes", 27, "Febrero", 2023]

# lista con listas
lista_d_listas = [["Alberto", 1.75, 80],
                  ["Ana", 1.70, 65],
                  ["María", 1.90, 80]]

# listas anidadas
lista_anidada = [["Stanley Kubrick", ["Senderos de Gloria", 1957]],
                 ["Woody Allen", ["Hannah y sus hermanas", 1986]]]


# EXTRAER ELEMNTOS DE UNA LISTA
# Primer elemento.
semana[0]
# Segundo elemento.
semana[1]
# Ultimo elemento.
semana[-1]

# Modificar elementos por su índice
semana[0] = "Astelehena"


# COMPROBAR EL TIPO DE DATO QUE ES UN ELEMENTO DE LA LISTA.
type(semana)
type(semana[-1])
type(enteros[-1])


# EXTRAER INTERVALOS.
lista_mixta[:3]
lista_mixta[1:3]
lista_mixta[-2:]
lista_mixta[-2:-1]
# del objeto 2 hasta el último
semana[2:]
# los tres primeros
semana[:3]
# los tres últimos
semana[-3:]
# Puedo usar los elementos extraidos para crear variables independientes (desempaquetado)
dia4, dia5, dia6 = semana[-3:]

# Longitud de una lista
len(semana)
len(lista_d_listas)
len(lista_anidada)


# CONCATENAR LISTAS.
# Unir listas consecutivamente
dias_numeros = semana + enteros
numeros_anidada = enteros + lista_anidada

# Concatenar cadenas dentro de una lista utilizando un separador.
semana_str1 = " o ".join(semana)
cadena_str2 = ", ".join(semana)


# REPETIR UNA LISTA
mes = 4 * semana


# COMPROBAR SI UN ELEMENTO EXISTE EN UNA LISTA
"Lunes" in semana
"Lunes" not in semana
"lunes" in semana
# Si buscamos el número como string no lo encuentra
"1" in enteros
1 in enteros


# CONTAR EL NUMERO DE VECES QUE APARECE UN ELEMENTO.
lista_anidada.count(1)
lista_anidada.count(["Stanley Kubrick", ["Senderos de Gloria", 1957]])
# No se accede a los elementos anidados
lista_anidada.count("Stanley Kubrick")


# Hacer una copia de una variable
lista_mixta_cp = lista_mixta[:]
lista_mixta_cp2 = lista_mixta.copy()
# OJO, no es lo mismo crear una copia que esignar una variable
lista_mixta_ref = lista_mixta
lista_mixta_ref.remove("Febrero")
# Mayo también ha sido eliminado de lista_mixta
lista_mixta


# ELIMINAR ELEMENTOS DE UNA LISTA
# Eliminar un elemento concreto
lista_mixta = ["Lunes", 27, "Febrero", 2023]
lista_mixta.remove(27)
lista_mixta.remove("Febrero")
lista_anidada.remove(["Stanley Kubrick", ["Senderos de Gloria", 1957]])


# Eliminar el ultimo elemento.
lista_mixta = ["Lunes", 27, "Febrero", 2023]
# Esta función SI modifica el original
lista_mixta.pop()
# Porque lo que devuelve es el objeto eliminado
lista_mixta


# Borrar los elementos de la lista.
lista_mixta_cp.clear()

# Eliminar la lista
del (lista_mixta_cp)
del (lista_mixta_cp2)


# ORDENAR UNA LISTA
# Por orden alfabetico (también modifica el original)
semana.sort()
semana

# Por orden numerico
# Cambiamos un elemento
enteros[0] = 5
enteros.sort()
enteros.sort(reverse=True)

# AÑADIR ELEMENTOS.
# Al final de la lista
enteros.append(17)

# Insertar elemento en un punto de una lista
enteros.insert(3, 12)  # Un 12 en la posicion 3 (empieza a contar de 0)
enteros.insert(3, "hola")  # Tambien pueden ser palabras.

# Extender una lista con datos de otra lista.
# Añadimos elementos a una lista
semana_cp = semana.copy()
semana_cp.extend(lista_anidada)
semana_cp

# Creamos un elemento nuevo (pisando el anterior)
# El resultado final es el mismo.
semana_ref = semana
semana_ref = semana + lista_anidada
semana_ref

# Meter Index

#########################
# TRABAJANDO CON TUPLAS #
#########################

# CREAMOS LAS TUPLAS
tupla_mixta = (1, 2, "tres", "cuatro", 5)
# Si la tupla sólo tiene un valor hay que añadir una coma al final
tupla = (1,)
# Si no, ignora el paréntesis
numero = (1)
# es posible no usar el paréntesis ya que tupla es el tipo por defecto de valores separados por comas
tupla_sin_parentesis = "casa", "Iturribide", 12

# También podemos hacer desempaquetado
vivienda, lugar, numero = tupla_sin_parentesis

# EXTRAEMOS ELEMENToS DE LAS TUPLAS
tupla_mixta[:2]
tupla_mixta[1:3]
tupla_mixta[2:-1]
tupla_mixta[2:]

# PERO NO SON MUTABLES
tupla_mixta[0] = 2
tupla_mixta.sort()
# La ventaja de esto es que pueden ser utilizadas como claves para los diccionarios

# MEDIMOS LA LONGITUD
len(tupla_mixta)

# CONCATENAR TUPLAS.
tupla_ampliada = tupla_mixta + tupla
len(tupla_ampliada)

# REPETICION DE TUPLAS
tupla_repe = 2 * tupla_mixta

# ANALIZAR SI EXISTE UN ELEMENTO
"tres" in tupla_mixta
"tre" in tupla_mixta
"tre" not in tupla_mixta


###############################
# TRABAJANDO CON DICCIONARIOS #
###############################

# CREAMOS EL DICCIONARIO
reyes_espana = {
    "Godos": ["Ataulfo", "Sigerico", "Teodorico", "Eurico", "Leovigildo", "Recaredo", "Suintila", "Sisenando", "Chintila", "Tulga", "Witerico", "Gundemaro", "Sisebuto", "Suintila II", "Recesvinto", "Wamba", "Ervigio", "Witiza", "Rodrigo"],
    "Austrias": ["Felipe I", "Carlos I", "Felipe II", "Felipe III", "Felipe IV", "Carlos II"],
    "Borbones": ["Felipe V", "Luis I", "Fernando VI", "Carlos III", "Carlos IV", "Fernando VII", "Isabel II", "Alfonso XII", "Alfonso XIII", "Juan Carlos I"]
}

# EXTRAEMOS LOS VALORES
lista_val = reyes_espana.values()

# Podemos extraer valores usando la clave
reyes_espana.get("Austrias")
reyes_espana.get("Austrias")[0]
# Pero no la clave con el valor
reyes_espana.get("Felipe I")
reyes_espana.keys()

# AÑADIR UN NUEVO ELEMENTO
reyes_espana['Saboya'] = ["Amadeo I"]
reyes_espana

# MODIFICAMOS UN ELEMENTO
reyes_espana['Saboya'] = "Amadeo último"
reyes_espana
reyes_espana.get("Austrias")[0] = "Felipe El Hermoso"
reyes_espana


#############
# Conjuntos #
#############
# El conjunto (set) es una colección desordenada de elementos únicos

# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
numeros = {1, 3, 2, 9, 3, 1}

# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
letras = set('Hola Pythonista')

# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
unicos = set([3, 5, 6, 1, 5, 17])

# Los elementos no son accesibles como en las listas (no están ordenados)
unicos[-2:]
# Pero sí son mutables como en las listas
unicos.remove(1)
# Si no está da error
unicos.remove(1)
# Y se debe usar discard
unicos.discard(17)

# Union
numeros | letras
# Intersección
numeros & unicos
