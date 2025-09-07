#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:42:28 2025

@author: juank
"""
import pandas as pd

d = {'nombre':['Antonio', 'Brenda', 'Camilo', 'David'], 'apellido': ['Restrepo', 'Saenz', 'Torres', 'Urondo'], 'lu': ['78/23', '449/22', '111/24', '1/21']}
df = pd.DataFrame(data = d) # creamos un df a partir de un diccionario
df.set_index('lu', inplace = True) 