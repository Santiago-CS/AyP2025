"""
==========================================================
PRÁCTICA INTEGRADORA: NumPy, pandas y matplotlib
==========================================================

Dataset: diabetes_dataset.csv

Columnas:
- gender               (object: 'Male', 'Female', 'Other')
- age                  (float)
- hypertension         (int: 0 = no, 1 = sí)
- heart_disease        (int: 0 = no, 1 = sí)
- bmi                  (float)
- hbA1c_level          (float)
- blood_glucose_level  (int)
- diabetes             (int: 0 = no, 1 = sí)

Objetivo general:
-----------------
Usar NumPy, pandas y matplotlib para explorar el dataset,
calcular estadísticas básicas, crear nuevas variables y
visualizar patrones relacionados con la diabetes.

Instrucciones generales:
------------------------
- Responde cada ejercicio en el espacio marcado con "TU CÓDIGO AQUÍ".
- No modifiques el nombre de las variables que se indican en cada punto.
- Al final, guarda el archivo como: practica_diabetes_tuNombre.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Para que los gráficos se vean con mejor tipografía (opcional)
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["axes.grid"] = True

# ==========================================================
# EJERCICIO 0. Carga de datos
# ==========================================================
# a) Carga el archivo "diabetes_dataset.csv" en un DataFrame llamado df.
# b) Muestra las primeras 5 filas.
# c) Muestra información general del DataFrame (df.info()).
# d) Imprime el número de filas y columnas (shape).

# === TU CÓDIGO AQUÍ ===
# df = ...
# print(...)
# ...

# ==========================================================
# EJERCICIO 1. Exploración básica con pandas
# ==========================================================
# a) Calcula la estadística descriptiva (describe) de las columnas numéricas.
# b) Obtén la distribución de la variable 'diabetes' (value_counts y proporciones).
# c) Obtén la distribución de la variable 'gender' (value_counts).

# === TU CÓDIGO AQUÍ ===
# desc = ...
# print(desc)
# dist_diabetes = ...
# print(dist_diabetes)
# dist_diabetes_prop = ...
# print(dist_diabetes_prop)
# dist_gender = ...
# print(dist_gender)

# ==========================================================
# EJERCICIO 2. Trabajo con NumPy y máscaras booleanas
# ==========================================================
# a) Extrae la columna 'age' como un arreglo de NumPy 'age_np'.
# b) Calcula la media, desviación estándar y mediana de la edad usando NumPy.
# c) Crea una máscara booleana 'mask_diab' para los pacientes con diabetes (diabetes == 1).
# d) Usando la máscara, calcula:
#    - La media de edad de pacientes con diabetes.
#    - La media de edad de pacientes sin diabetes.

# === TU CÓDIGO AQUÍ ===
# age_np = ...
# mean_age = ...
# std_age = ...
# median_age = ...
# mask_diab = ...
# mean_age_diab = ...
# mean_age_no_diab = ...

# ==========================================================
# EJERCICIO 3. Índice de riesgo con NumPy (feature engineering)
# ==========================================================
# Supón que queremos construir un indicador sencillo de "riesgo" de diabetes
# combinando tres variables numéricas:
# - bmi
# - hbA1c_level
# - blood_glucose_level
#
# a) Normaliza cada una de estas columnas restando la media y dividiendo entre la desviación estándar.
#    (usa NumPy: (x - x.mean()) / x.std())
# b) Crea un nuevo arreglo llamado 'risk_index_np' definiendo:
#    risk_index = 0.4 * bmi_norm + 0.3 * hbA1c_norm + 0.3 * glucose_norm
# c) Agrega este índice al DataFrame como columna 'risk_index'.

# === TU CÓDIGO AQUÍ ===
# bmi = ...
# hb = ...
# glu = ...
# bmi_norm = ...
# hb_norm = ...
# glu_norm = ...
# risk_index_np = ...
# df["risk_index"] = ...

# ==========================================================
# EJERCICIO 4. Agrupaciones con pandas (groupby)
# ==========================================================
# a) Calcula la tasa de diabetes (promedio de la columna 'diabetes') por 'gender'.
# b) Calcula, por género, la media de 'age', 'bmi' y 'risk_index'.
# c) Ordena los resultados anteriores de mayor a menor tasa de diabetes.

# === TU CÓDIGO AQUÍ ===
# tasa_diabetes_gender = ...
# print(tasa_diabetes_gender)
# stats_gender = ...
# print(stats_gender)


# ==========================================================
# EJERCICIO 5. Tablas de contingencia (crosstab)
# ==========================================================
# a) Construye una tabla de contingencia entre 'hypertension' y 'diabetes'.
# b) Construye otra tabla de contingencia normalizada por filas para obtener
#    las proporciones de diabéticos dentro de cada categoría de 'hypertension'.

# === TU CÓDIGO AQUÍ ===
# tab_htn = ...
# print(tab_htn)
# tab_htn_prop = ...
# print(tab_htn_prop)



# ==========================================================
# EJERCICIO 6. Visualización 1: Histogramas
# ==========================================================
# a) Grafica un histograma de la variable 'age'.
# b) Grafica un histograma de la variable 'bmi' solamente para pacientes con diabetes.
# c) Grafica un histograma de 'bmi' para pacientes sin diabetes.
#    (Puedes superponer ambas distribuciones o hacer 2 gráficos separados.)

# === TU CÓDIGO AQUÍ ===
# plt.figure()
# ...
# plt.show()


# ==========================================================
# EJERCICIO 7. Visualización 2: Boxplots
# ==========================================================
# a) Crea un boxplot de 'blood_glucose_level' separado por 'diabetes'
#    (0 y 1 en el eje x).
# b) Interpreta visualmente si hay diferencia en los niveles de glucosa
#    entre pacientes con y sin diabetes.

# === TU CÓDIGO AQUÍ ===
# data_no_diab = ...
# data_diab = ...
# plt.figure()
# ...
# plt.show()


# ==========================================================
# EJERCICIO 8. Visualización 3: Dispersión (scatter plot)
# ==========================================================
# a) Crea un scatter plot de 'age' (eje x) vs 'blood_glucose_level' (eje y).
# b) Colorea los puntos según la variable 'diabetes' (0 ó 1).
#    Pista: puedes usar un arreglo de colores con NumPy.

# === TU CÓDIGO AQUÍ ===
# x = ...
# y = ...
# colores = ...
# plt.figure()
# ...
# plt.show()


# ==========================================================
# EJERCICIO 9. Mini proyecto integrador
# ==========================================================
# Objetivo:
# Crear un pequeño análisis que responda la pregunta:
#   "¿Quiénes parecen tener mayor riesgo de diabetes en este dataset?"
#
# a) Elige un subconjunto del DataFrame filtrando por:
#    - edad mayor o igual a 40 años
#    - y/o presencia de hipertensión o enfermedad cardíaca
# b) Calcula para ese subconjunto:
#    - tasa de diabetes
#    - media de risk_index
# c) Compáralo contra la población general.
# d) Genera al menos una gráfica (a tu elección) para ilustrar la comparación.
#
# Puedes usar todas las herramientas anteriores (NumPy, pandas, matplotlib).

# === TU CÓDIGO AQUÍ ===
# filtro = ...
# df_sub = ...
# tasa_diab_sub = ...
# tasa_diab_total = ...
# print(...)
# plt.figure()
# ...
# plt.show()

