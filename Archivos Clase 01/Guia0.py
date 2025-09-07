#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 12:14:59 2025

@author: juank
"""

# Ejercicio 1
def contar_billetes(espesor, alto_max):
    alto = 0
    k = 0
    while (alto <= alto_max):
        alto = alto + espesor
        k += 1
    return k

print(contar_billetes(0.00011,67.5))

# Ejercicio 2
def cadena_geringosa_for(cadena):
    cadena_geringosa = ''
    vocales = ['a','e','i','o','u']
    for c in cadena:
        if (c in vocales):
            cadena_geringosa = cadena_geringosa + c + 'p' + c
        else:
            cadena_geringosa = cadena_geringosa + c
    return cadena_geringosa

print(cadena_geringosa_for('Casa'))

def cadena_geringosa_while(cadena):
    cadena_geringosa = ''
    vocales = ['a','e','i','o','u']
    k = 0
    while (k < len(cadena)):
        c = cadena[k]
        if (c in vocales):
            cadena_geringosa = cadena_geringosa + c + 'p' + c
        else:
            cadena_geringosa = cadena_geringosa + c
        k+=1
    return cadena_geringosa

print(cadena_geringosa_while('Casa'))

# Ejercicio 3
def pertenece(lista, elem):
    k = 0
    c = False
    while (k < len(lista)):
        if (lista[k]==elem):
            c = True
            break
        k+=1
    return c

print(pertenece(['a','a','a','b','a','a','d'],'c'))
print(pertenece(['a','a','a','b','a','a','d'],'b'))
print(pertenece(['a','a','a','b','a','a','d'],'d'))

# Ejercicio 4
def mas_larga(lista1, lista2):
    if (len(lista1) > len(lista2)):
        lista = lista1
    elif (len(lista1) < len(lista2)):
        lista = lista2
    else:
        lista = []
    return lista

print(mas_larga(['a','a','a','b','a','a','d'],['a','a','a','b','a','a']))


# Ejercicio 5
def rebotes(altura,n):
    print(altura)
    for k in range(0,n):
        altura = altura*3/5
        print(altura)
    return

rebotes(100,10)

# Ejercicio 6
def mezclar(lista1,lista2):
    lista = ''
    while (len(lista1)>0 or len(lista2)>0):
        if (len(lista1)>0):
            lista = lista+lista1[0]
            lista1=lista1[1:]
        if (len(lista2)>0):
            lista = lista+lista2[0]
            lista2=lista2[1:]
    return lista
            
print(mezclar('Pepe','Jose'))
print(mezclar('Pepe','Josefa'))

# Ejercicio 7
# Ejercicio 8
def traductor_jeringoso(lista):
    d = {}
    for l in lista:
        d[l] = cadena_geringosa_while(l)
    return d

print(traductor_jeringoso(['Pepe','Josefa']))

# Ejercicio 9


