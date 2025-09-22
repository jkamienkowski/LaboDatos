#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 19:42:21 2025

@author: mcerdeiro
"""
#%% importar módulos

import pandas as pd
import duckdb

print("DuckDB version:", duckdb.__version__)
#%% cargar los archivos

carpeta = "Dengue_Zika_SQL/" # carpeta donde están los csv requeridos

# Datasets
casos           = pd.read_csv(carpeta+"casos.csv")
departamentos   = pd.read_csv(carpeta+"departamentos.csv")
grupoetario     = pd.read_csv(carpeta+"grupoetario.csv")
provincia       = pd.read_csv(carpeta+"provincia.csv")
tipoevento      = pd.read_csv(carpeta+"tipoevento.csv")

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

