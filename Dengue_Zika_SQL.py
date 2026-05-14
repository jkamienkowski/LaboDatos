#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 19:42:21 2025

@author: mcerdeiro
"""
#%% importar módulos

import pandas as pd
import duckdb
#%% cargar los archivos

carpeta = "/home/juank/repos/LaboDatos/Guía Práctica - SQL - Dengue_Zika/" # carpeta donde están los csv requeridos

# Datasets
casos           = pd.read_csv(carpeta+"casos.csv")
departamento    = pd.read_csv(carpeta+"departamento.csv")
grupoetario     = pd.read_csv(carpeta+"grupoetario.csv")
provincia       = pd.read_csv(carpeta+"provincia.csv")
tipoevento      = pd.read_csv(carpeta+"tipoevento.csv")

#%%
# Ejemplo inicial
print(departamento)

consultaSQL = """
    SELECT DISTINCT descripcion
    FROM departamento
    WHERE id_provincia==54;
"""

resultado = duckdb.sql(consultaSQL).df()

print(resultado)
#%%
# === Ejercicios ===


consultaSQL = """
    SELECT *
    FROM provincia
    WHERE descripcion = 'Chaco';
"""

chaco = duckdb.sql(consultaSQL).df()

print(chaco)

consultaSQL = """
    SELECT DISTINCT *
    FROM departamento
    INNER JOIN chaco
    ON id_provincia==chaco.id;
"""

resultado = duckdb.sql(consultaSQL).df()

print(resultado)

consultaSQL = """
    SELECT DISTINCT d.*
    FROM departamento AS d
    INNER JOIN provincia AS p
    ON d.id_provincia = p.id
    WHERE p.descripcion = 'Chaco';
"""
resultado = duckdb.sql(consultaSQL).df()
print(resultado)

#%%
#resultado = duckdb.sql(consultaSQL).fetchone()[0]

consultaSQL = """
    SELECT anio,id_tipoevento,count(*) AS CantidadCasos
    FROM casos
    WHERE anio = 2019
    GROUP BY (anio,id_tipoevento)
    ORDER BY anio
"""
resultado = duckdb.sql(consultaSQL).df()
print(resultado)

consultaSQL = """
    SELECT c1.anio,c1.id_tipoevento
    FROM casos AS c1
    WHERE c1.anio = ALL (
        SELECT count(*)
        FROM casos AS c2
        WHERE c2.anio = c1.anio
        )
"""
resultado = duckdb.sql(consultaSQL).df()
print(resultado)



