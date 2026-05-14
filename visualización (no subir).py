#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase Visualizacion. Script clase.
Autor  : Ailen Altamirano
Fecha  : 2024-01-04
"""
#%%
# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Carpeta donde se encuentran los archivos a utilizar
carpeta = "data-visualizacion/"

#%% Parámetros globales de matplotlib
plt.rcParams['font.family'] = 'sans-serif'        
plt.rcParams['font.size'] = 9.0


#%%############################################################################
#                                                                             #
#                          Nuestros primeros gráficos                         #
#                                                                             #
###############################################################################

wine = pd.read_csv(carpeta+"wine.csv", sep = ";")   
# con sep indicamos que el separador es ;
cheetahRegion = pd.read_csv(carpeta+"cheetahRegion.csv")
gaseosas= pd.read_csv(carpeta+"gaseosas.csv")
ageAtDeath= pd.read_csv(carpeta+"ageAtDeath.csv")

#%%## SCATTER PLOT

# Genera el grafico que relaciona la acidez (no volatil) y el contenido de 
# acido citrico de cada vino
plt.scatter(data = wine, x='fixed acidity', y='citric acid')


# Genera el grafico que relaciona  la acidez (no volatil) 
# y el contenido de  acido citrico (cambiamos algunos 
# parametros para mejorar la informacion mostrada)
fig, ax = plt.subplots() 

# plt.subplots() es una función que devuelve una tupla que contiene: 
# i)  el objeto correspondiente a una figura
# ii) el objeto correspondiente a sus ejes
# 
# Contar con fig es útil si quiere cambiar los atributos a nivel de figura o 
# guardar la figura como un archivo de imagen más adelante, por ejemplo con 
# fig.savefig('yourfilename.png')


# ax.scatter(wine['fixed acidity'], wine['citric acid'])   # Otra manera
ax.scatter(data = wine,  
           x='fixed acidity', 
           y='citric acid',
           s=8,                       # Tamano de los puntos
           color='magenta')           # Color de los puntos

ax.set_title('Acidez vs contenido de ácido cítrico') # Titulo del gráfico
ax.set_xlabel('Acidez (g/dm3)', fontsize='medium')   # Nombre eje X           
ax.set_ylabel('Contenido de ácido cítrico (g/dm3)', 
              fontsize='medium')                     # Nombre eje Y


#%%### BUBBLE CHART - Variación del scatter con tercer variable CONTINUA

# Genera el grafico que relaciona tres variables en simultaneo 
# (grafico por defecto)
plt.scatter(data=wine, x='fixed acidity', y='citric acid', s='residual sugar')

# Genera el grafico que relaciona tres variables en simultaneo 
# (mejorando la informacion mostrada)
fig, ax = plt.subplots()

tamanoBurbuja = 5  

ax.scatter(data=wine, x='fixed acidity', 
           y='citric acid', s=wine['residual sugar']*tamanoBurbuja)

ax.set_title('Relación entre tres variables')
ax.set_xlabel('Acidez (g/dm3)', fontsize='medium')                       
ax.set_ylabel('Contenido de ácido cítrico (g/dm3)', 
              fontsize='medium')    


# remueve la variable remporal tamanoBuebuja que ya no utilizaremos
del tamanoBurbuja 

#%%## SCATTER PLOT - con Color para tercer variable DISCRETA

# Genera el grafico que relaciona tres variables en simultaneo 
fig, ax = plt.subplots()

wine_blanco = wine[wine['type'] == 'white']
wine_tinto  = wine[wine['type'] == 'red']

ax.scatter(data=wine_blanco, x='fixed acidity', 
           y='citric acid', c='yellow', edgecolor='k', label='blanco')

ax.scatter(data=wine_tinto, x='fixed acidity', 
           y='citric acid', c='red', edgecolor='k', label='tinto')


ax.set_title('Relación entre tres variables')
ax.set_xlabel('Acidez (g/dm3)', fontsize='medium')                       
ax.set_ylabel('Contenido de ácido cítrico (g/dm3)', 
              fontsize='medium')    
ax.legend()

del wine_blanco, wine_tinto

# %%===========================================================================
#                                  Ejercicios
# =============================================================================
# Sigamos trabajando con el dataset de vinos

# ¿Existe alguna relación entre el pH de los vinos (pH) y alguna de las 
# otras variables? Muestrelo gráficamente 

# Discutir con el resto de la clase:
# ¿Cuál fue su objetivo: Explorar, Explicar, Otro?
# ¿Qué tipos de variables estaban en juego?
# ¿Mejoró alguna característica del gráfico para cumplir con el objetivo?

# Posible solucion
fig, ax = plt.subplots() 
ax.scatter(data = wine,  
           x='sulphates', 
           y='pH',
           s=8,
           color='magenta')

ax.set_title('pH vs contenido de sulfatos') 
ax.set_ylabel('pH', fontsize='medium')   
ax.set_xlabel('Contenido de sulfatos (g/dm3)',  
              fontsize='medium')         

# En el gráfico puede observarse que el pH aumenta cuando
# aumenta el contenido de sulfatos
# Dado que lo que se busca es relacionar dos variables de tipo
# cuantitativo, se eligió realizar un scatter plot

#%%### GRAFICO DE LINEAS

# Genera el grafico de la serie temporal (grafico por defecto)
plt.plot('Anio', 'Ventas', data=cheetahRegion)

# Genera el grafico de la serie temporal (mejorando la informacion mostrada)
fig, ax = plt.subplots()

ax.plot('Anio', 'Ventas', data=cheetahRegion, marker="o")

ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 12)
ax.set_ylim(0, 250)


#%%## GRAFICO DE LINEAS - con Color para tercer variable discreta

# Genera el grafico de ambas series temporales
fig, ax = plt.subplots()

# Grafica la serie regionEste 
ax.plot('Anio', 'regionEste', data=cheetahRegion, 
        marker='.',            # Tipo de punto (punto, circulo, estrella, etc.)
        linestyle='-',         # Tipo de linea (solida, punteada, etc.)
        linewidth=0.5,         # Ancho de linea 
        label='Región Este',   # Etiqueta que va a mostrarse en la leyenda
        )

# Grafica la serie regionOeste
ax.plot('Anio', 'regionOeste', data=cheetahRegion, 
        marker='.', 
        linestyle='-',
        linewidth=0.5,
        label='Región Oeste'
        )

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Ventas de la compañía Cheetah Sports según región')
ax.set_xlabel('Año')
ax.set_ylabel('Ventas (millones de $)')
ax.set_xlim(0,12)
ax.set_ylim(0,140)

# Muestra la leyenda
ax.legend()

# %%===========================================================================
#                                  Ejercicios
# =============================================================================

# Sean los siguientes datos correspondientes a los precios del 
# biodiesel en distintos períodos en la Argentina
# (se encuentran subidos en el campus) 


# Generar un gráfico para representarlos gráficamente
# Analizar los resultados obtenidos
# Discutir con el resto de la clase
# ¿Cuál fue su objetivo: Explorar, Explicar, Otro?
# ¿Qué tipos de variables estaban en juego?
# ¿Qué tipo de gráfico decidió utilizar?
# ¿Qué resultados obtuvo?
# ¿Mejoró alguna característica del gráfico para cumplir con el objetivo?

# Cargamos dataset del precioBiodiesel
precioBiodiesel= pd.read_csv(carpeta+"precioBiodiesel.csv")    


# Genera el grafico de precio Biodiesel
fig, ax = plt.subplots()

ax.plot('Periodo', 'Precio', 
        data=precioBiodiesel.sort_values('Periodo', ascending=True),
        marker=".")

ax.set_title('Evolución del Precio del Biodiesel')
ax.set_xlabel('Periodo', fontsize='medium')                       
ax.set_ylabel('Precio ($)', fontsize='medium')    
plt.xticks(rotation = 60, fontsize=7)


#%%## GRAFICO DE BARRAS (BAR PLOT)
# Volvamos al cheetahRegion que usamos para el Line Plot
# ¿Por qué podemos usar un BarPlot?

# Genera el grafico de barras de las ventas mensuales
fig, ax = plt.subplots()

ax.bar(data=cheetahRegion, x='Anio', height='Ventas')
       
ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 11)
ax.set_ylim(0, 250)

ax.set_xticks(range(1,11,1))                # Muestra todos los ticks del eje x
ax.set_yticks([])                           # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)  # Agrega la etiqueta a cada barra


#%%## GRAFICO DE BARRAS AGRUPADAS
# Genera el grafico de barras de ambas series temporales
fig, ax = plt.subplots()

cheetahRegion.plot(x='Anio', 
            y=['regionEste', 'regionOeste'], 
            kind='bar',
            label=['Region Este', 'Region Oeste'],# Agrega etiquetas a la serie
            ax = ax)

ax.set_title('Ventas de la compañía Cheetah Sports según región')
ax.set_xlabel('Año')
ax.set_ylabel('Ventas (millones de $)')
ax.set_xlim(-1,10)
ax.set_ylim(0,140)


#%%## GRAFICO DE BARRAS APILADAS

# Genera el grafico de barras apiladas de ambas series temporales
fig, ax = plt.subplots()

# Grafica la serie regionEste 
ax.bar(cheetahRegion['Anio'], cheetahRegion['regionEste'] , 
       label='Region Este', color = "#4A4063")
# Grafica la serie regionOeste
ax.bar(cheetahRegion['Anio'], cheetahRegion['regionOeste'], 
       bottom=cheetahRegion['regionEste'], label='Region Oeste',
       color = '#BFACC8')

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Ventas de la compañía Cheetah Sports según región')
ax.set_xlabel('Año')
ax.set_ylabel('Ventas (millones de $)')
ax.set_xlim(0,10.9)
ax.set_ylim(0,250)
ax.set_xticks(range(1,11,1))    

plt.legend()                    

#%%## PIE PLOT

# Contamos cuantos vinos de cada tipo hay en el dataset
wine['type'].value_counts()

# Transformamos la salida de value_counts enun dataframe
conteos = pd.DataFrame(wine['type'].value_counts()).reset_index()
conteos = conteos.rename(columns={'index': 'type', 0: 'count'})

# Genera el grafico de torta (grafico por defecto)
plt.pie(data=conteos, x='count')


# Genera el grafico de barras torta (mejorando la informacion mostrada)
fig, ax = plt.subplots()

ax.pie(data=conteos, 
       x='count', 
       labels='type',           # Etiquetas
       autopct='%1.2f%%',       # porcentajes
       colors=['gold',
               'purple'],
       shadow = True, 
       explode = (0.1,0)        # separa las slices del pie plot
       )





#%%##
# Sean los siguientes datos correspondientes a 
# poseedores de teléfonos 
# (se encuentran subidos en el campus) 


# Generar un gráfico para representarlos gráficamente
# Analizar los resultados obtenidos
# Discutir con el resto de la clase
# ¿Cuál fue su objetivo: Explorar, Explicar, Otro?
# ¿Qué tipos de variables estaban en juego?
# ¿Qué tipo de gráfico decidió utilizar?
# ¿Qué resultados obtuvo?
# ¿Mejoró alguna característica del gráfico para cumplir con el objetivo?
# Responder Verdadero o Falso y justificar visualmente. 
# “Es más probable que las personas mayores posean un teléfono 
# inteligente a que las personas más jóvenes posean uno inteligente.”

# Cargamos dataset del precioBiodiesel
telefonosInteligentes= pd.read_csv(carpeta+"telefonosInteligentes.csv")    

    
# Genera el grafico de poseedores de telefonos 
# Elijo usar un grafico de barras apiladas
fig, ax = plt.subplots()

# Grafica la serie Telefono Inteligente
ax.bar(telefonosInteligentes['RangoEtario'],
       telefonosInteligentes['Telefono_Inteligente'],
       label='Teléfono Inteligente' )
# Grafica la serie Telefono No Inteligente
ax.bar(telefonosInteligentes['RangoEtario'],
       telefonosInteligentes['Telefono_NoInteligente'],
       bottom=telefonosInteligentes['Telefono_Inteligente'],
       label='Teléfono No Inteligente')
# Grafica la serie Sin Telefono
ax.bar(telefonosInteligentes['RangoEtario'],
       telefonosInteligentes['SinTelefono'],
       bottom=   telefonosInteligentes['Telefono_Inteligente']
               + telefonosInteligentes['Telefono_NoInteligente'],
       label='Sin Teléfono')

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Distribución de Poseedores de Teléfonos según Rango Etario')
ax.set_xlabel('Rango Etario')
ax.set_ylabel('% de Personas')
ax.set_ylim(0,105)
   

# Muestra la leyenda
fig.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.55, 1.1))

#%%############################################################################
#                                                                             #
#                          Distribución de los datos                          #
#                                                                             #
###############################################################################

# %%===========================================================================
#                              Datos Categóricos
# =============================================================================

# Mostramos las primeras observaciones
gaseosas.head()

# Tabla de frecuencias
gaseosas['Compras_gaseosas'].value_counts()    

# Genera el grafico de frecuencias (grafico por defecto)
gaseosas['Compras_gaseosas'].value_counts().plot.bar()


# Genera el grafico de frecuencias (mejorando la informacion mostrada)
fig, ax = plt.subplots()
gaseosas['Compras_gaseosas'].value_counts().plot.bar(ax = ax)

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas de gaseosas') 
ax.set_yticks([])                             # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)    # Agrega la etiqueta a cada barra
ax.tick_params(axis='x', labelrotation=0)     # Rota las etiquetas del eje x

# Eliminar lineas del recuadro
ax.spines[['right', 'top', 'left']].set_visible(False) 

#%%### Frecuencias relativas
fig, ax = plt.subplots()

ax = gaseosas['Compras_gaseosas'].value_counts(normalize=True).plot.bar()


# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Frecuencia Relativa de Venta de Gaseosas')
ax.set_xlabel('Marcas de gaseosas') 
ax.set_yticks([])     
ax.bar_label(ax.containers[0], fontsize=8)     
ax.tick_params(axis='x', labelrotation=0)     
ax.spines[['right', 'top', 'left']].set_visible(False)

# En formato porcentual
# ax.set_title('Frecuencia Porcentual de Venta de Gaseosas')
# ax.bar_label(ax.containers[0], fontsize=8, fmt='{:.2%}') 
                    # Agrega la etiqueta a cada barra en formato de porcentaje



# %%===========================================================================
#                           Continuos - Histograma
# =============================================================================

#%%
ageAtDeath.head()

# Genera el grafico de frecuencias como con las variables categoricas
ageAtDeath['AgeAtDeath'].sort_values().value_counts(sort=False).plot.bar()


fig, ax = plt.subplots()

# Calculamos datos necesarios para generar las barras
width = 7                          # Cada esta cantidad de anios
bins = np.arange(1,114, width)     # Desde 1 a 114 (inclusive) cada width anios

# Contamos cuantos de los datos caen en cada uno de los bins
counts, bins = np.histogram(ageAtDeath['AgeAtDeath'], bins=bins)

# Fijamos la ubicacion de cada bin
center = (bins[:-1] + bins[1:]) / 2         # Calcula el centro de cada barra

ax.bar(x=center,            # Ubicacion en el eje x de cada bin
       height=counts,       # Alto de la barra
       width=width,         # Ancho de la barra
       align='center',      # Barra centrada
       color='skyblue',     # Color de la barra
       edgecolor='black')   # Color del borde de la barra


ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Cantidad de personas')
ax.spines[['right', 'top']].set_visible(False) 


# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]        # Define los limites de los bins

# Genera el string de los labels del estilo (v1, v2]
labels =  [f'({int(edge)},{int(bin_edges[i+1])}]'  
           for i, edge in enumerate(bin_edges[:-1])] 

ax.set_xticks(center)                          # Ubica los ticks del eje x
# Asigna labels a los ticks del eje x
ax.set_xticklabels(labels, rotation=90, fontsize=12)
ax.tick_params(axis ='x', length = 6, width =2)                 



# %%===========================================================================
#                  Añadiendo una tercer variable - Histograma
# =============================================================================
#%% 
# Armamos dos subsets: Male y Female
obsFemale = ageAtDeath[ageAtDeath['Sex']=='Female']['AgeAtDeath']
obsMale   = ageAtDeath[ageAtDeath['Sex']=='Male'  ]['AgeAtDeath']


fig, ax = plt.subplots()

# Calculamos datos necesarios para generar las barras
width = 7                                        
bins = np.arange(1,114, width)     

# Contamos cuantos de los datos caen en cada uno de los bins
countsFemale, bins = np.histogram(obsFemale, bins=bins)
countsMale  , bins = np.histogram(obsMale  , bins=bins)

# Si queremos graficar la frecuencia en vez de la cantidad, la calculamos
freqFemale = countsFemale / float(countsFemale.sum())
freqMale   = countsMale   / float(countsMale.sum())


# Fijamos la ubicacion de cada bin
center = (bins[:-1] + bins[1:]) / 2

# Graficamos Female
ax.bar(x=center-width*0.15,         # Corremos para la izquierda del centro
   height=countsFemale, 
   width=width*.3,                  # Ajustamos el ancho
   align='center',      
   color='orange',     
   edgecolor='black')

# Graficamos Male
ax.bar(x=center+width*0.15,         # Corremos para la derecha del centro
   height=countsMale,   
   width=width*.3,                  # Ajustamos el ancho
   align='center',      
   color='skyblue',     
   edgecolor='black')   


ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Cantidad de personas')


# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
       for i, edge in enumerate(bin_edges[:-1])] 

ax.set_xticks(center)
ax.set_xticklabels(labels, rotation=90, fontsize=12) 
ax.tick_params(axis ='x', length = 6, width =2)

ax.legend(['Femenino', 'Masculino'], loc='upper left')


#%%## Graficamos la frecuencia relativa

fig, ax = plt.subplots()

# Graficamos Female
ax.bar(x=center-width*0.15,        
   height=freqFemale,       # Usamos freqFemale
   width=width*.3,    
   align='center',    
   color='orange',    
   edgecolor='black') 

# Graficamos Male
ax.bar(x=center+width*0.15,
   height=freqMale,         # Usamos freqMale
   width=width*.3,    
   align='center',    
   color='skyblue',   
   edgecolor='black') 

ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Frecuencia Relativa de Cantidad de personas')


bin_edges = [max(0, i-1) for i in bins]

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
       for i, edge in enumerate(bin_edges[:-1])] 

ax.set_xticks(center)                        
ax.set_xticklabels(labels, rotation=90, fontsize=12)
ax.tick_params(axis ='x', length = 6, width =2)                 

ax.legend(['Femenino', 'Masculino'], loc='upper left')



# %%===========================================================================
#                                  Ejercicios
# =============================================================================
# Sean los datos correspondientes a las propinas de un bar 
# (están cargados en el campus en el archivo tips.csv)
# Generar un gráfico para analizar la distribución de la propina en función del:
# Sexo
# Día de la semana
# Comentar los resultados obtenidos

################ DISTRIBUCION DE PROPINA EN FUNCION DEL SEXO ################
tips = pd.read_csv(carpeta+"tips.csv")

# Armamos dos subsets: Male y Female
obsFemale=tips[tips['sex']=='Female']['tip']
obsMale  =tips[tips['sex']=='Male']['tip']

fig, ax = plt.subplots()

# Calculamos datos necesarios para generar las barras
width = 1       # Cada esta cantidad de anios
bins = np.arange(1,13, width)

countsFemale, bins = np.histogram(obsFemale, bins=bins)
countsMale  , bins = np.histogram(obsMale  , bins=bins)

freqFemale = countsFemale / float(countsFemale.sum())
freqMale   = countsMale   / float(countsMale.sum())

center = (bins[:-1] + bins[1:]) / 2

# Graficamos Female
ax.bar(x=center-width*0.2,        
   height=countsFemale,     
   width=width*.4,         
   align='center',      
   color='orange',     
   edgecolor='black')   

# Graficamos Male
ax.bar(x=center+width*0.2,
   height=countsMale,
   width=width*.4,
   align='center',
   color='skyblue',
   edgecolor='black')


ax.set_title('Distribución de propinas recibidas')
ax.set_xlabel('Propina recibida ($)')
ax.set_ylabel('Cantidad de personas')
ax.set_ylim(0,57)


bin_edges = [max(0, i-1) for i in bins]

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
       for i, edge in enumerate(bin_edges[:-1])] 

ax.set_xticks(bin_edges[:-1])
ax.set_xticklabels(labels, rotation=45, fontsize=12) 
ax.tick_params(bottom = False)

#Agrega leyenda
ax.legend(['Femenino', 'Masculino'], loc='upper left')

#%%######### DISTRIBUCION DE LA PROPINA EN FUNCION DEL DIA ###############
# Armamos dos subsets: Male y Female
obsSat=tips[tips['day']=='Sat']['tip']
obsSun=tips[tips['day']=='Sun']['tip']
obsThur=tips[tips['day']=='Thur']['tip']
obsFri=tips[tips['day']=='Fri']['tip']

fig, ax = plt.subplots()

# Calculamos datos necesarios para generar las barras
width = 1
bins = np.arange(1,13, width)

# Contamos cuantos de los datos caen en cada uno de los bins
countsSat, bins = np.histogram(obsSat, bins=bins)
countsSun, bins = np.histogram(obsSun, bins=bins)
countsThur, bins = np.histogram(obsThur, bins=bins)
countsFri, bins = np.histogram(obsFri, bins=bins)


center = (bins[:-1] + bins[1:]) / 2

# Graficamos Sabados
ax.bar(x=center - width *0.5,
   height=countsSat,
   width=width*.2,
   align='center',
   color='#230007',
   edgecolor='black')

# Graficamos Domingos
ax.bar(x=center - width *0.3,
   height=countsSun,
   width=width*.2,
   align='center',
   color='#D7CF07',
   edgecolor='black')

# Graficamos Jueves
ax.bar(x=center - width*0.1,
   height=countsThur,
   width=width*.2,
   align='center',
   color='#D98324',
   edgecolor='black')

# Graficamos Viernes     
ax.bar(x=center+width*0.1,
   height=countsFri,
   width=width*.2,
   align='center',
   color='#A40606',
   edgecolor='black')


ax.set_title('Distribución de propinas recibidas')
ax.set_xlabel('Propina recibida ($)')
ax.set_ylabel('Cantidad de personas')
ax.set_ylim(0,30)


bin_edges = [max(0, i-1) for i in bins]

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
       for i, edge in enumerate(bin_edges[:-1])]

ax.set_xticks(bin_edges[:-1])
ax.set_xticklabels(labels, rotation=45, fontsize=12)
ax.tick_params(bottom = False)                      
ax.legend(['Sabados', 'Domingos', 'Jueves', 'Viernes'], loc='upper right')
