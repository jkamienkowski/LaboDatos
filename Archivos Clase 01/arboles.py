#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:59:32 2025

@author: juank
"""

import pandas as pd
ruta = '/home/juank/repos/LaboDatos/'
archivo = '/home/juank/repos/LaboDatos/arbolado-en-espacios-verdes.csv'
df = pd.read_csv(archivo, index_col = 2)