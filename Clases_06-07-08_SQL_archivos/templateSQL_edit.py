#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 19:42:21 2025

@author: mcerdeiro
"""

import sys
print(sys.executable)
print(sys.path[:3])  # primeras 3 rutas

#%% importar módulos

import pandas as pd
import duckdb
#%% cargar los archivos

carpeta = "" # carpeta donde están los csv requeridos

# Datasets
empleado       = pd.read_csv(carpeta+"empleado.csv")
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
se_inscribe_en = pd.read_csv(carpeta+"se_inscribe_en.csv")
materia        = pd.read_csv(carpeta+"materia.csv")
vuelo          = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto     = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero       = pd.read_csv(carpeta+"pasajero.csv")    
reserva        = pd.read_csv(carpeta+"reserva.csv")    
empleadoRol    = pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto    = pd.read_csv(carpeta+"rolProyecto.csv")    
examen         = pd.read_csv(carpeta+"examen.csv")
examen03       = pd.read_csv(carpeta+"examen03.csv")

#%%
# Ejemplo inicial
print(empleado)

consultaSQL = """
    SELECT DISTINCT DNI, Salario
    FROM empleado;
"""

resultado = duckdb.sql(consultaSQL).df()

print(resultado)
#%%
# === Ejercicios ===

consultaSQL = """
---- completar consulta """
resultado = duckdb.sql(consultaSQL).df()

