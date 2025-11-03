# 15.- USO DE BIBLIOTECAS DE FUNCIONES (STANDARD LIBRARY BÁSICA)
# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UN MÓDULO?
# ---------------------------------------------------------------
# - Un MÓDULO es un archivo con funciones, clases y constantes reutilizables.
# - La BIBLIOTECA ESTÁNDAR de Python incluye muchos módulos listos para usar.
# - Formas de importación (recomendaciones para cursos iniciales):
#
#   1) import nombre_modulo
#      Luego: nombre_modulo.funcion(...)
#
#   2) from nombre_modulo import nombre
#      Luego: nombre(...)
#
#   3) import nombre_modulo as alias
#      Luego: alias.funcion(...)
#
# - Evita importar con * (from modulo import *) en cursos iniciales porque contamina el espacio de nombres.
#
# - Depuración: puedes imprimir valores intermedios y usar una bandera DEBUG global para activar/desactivar trazas.

# ---------------------------------------------------------------
# C) MÓDULO math: CONSTANTES Y FUNCIONES NUMÉRICAS
# ---------------------------------------------------------------
import math

# Constantes:
print(math.pi)          # π
print(math.e)           # e

# Raíz cuadrada (dominio: x >= 0):
try:
    print(math.sqrt(25))
    # print("sqrt(-1) ->", math.sqrt(-1))  # ValueError
except ValueError:
    print("ValueError: dominio inválido")

# Potencias y valores absolutos (pow, fabs):
print(math.pow(2, 10))   
print(math.fabs(-3.5))   

# Piso y techo (enteros):
print(math.floor(3.7))   
print(math.ceil(3.1))    

# Conversión grados<->radianes y trigonometría básica:
deg = 30
rad = math.radians(deg)
print(rad)
print(math.sin(rad))
print(math.cos(rad))

# Comparación con tolerancia (flotantes): math.isclose
a = 0.1 + 0.2
b = 0.3
print("0.1+0.2 == 0.3 ?", (a == b))
print(math.isclose(a, b, rel_tol=1e-9))

# ---------------------------------------------------------------
# D) MÓDULO random: ALEATORIEDAD Y REPRODUCIBILIDAD
# ---------------------------------------------------------------
import random

# Semilla: fija la secuencia (útil para depurar o reproducir ejemplos)
random.seed(12345)

# Enteros aleatorios en [a, b] (incluye extremos):
print(random.randint(1,6))

# choice: elige un elemento de una lista no vacía
faces = ["A", "B", "C", "D"]
print(random.choice(faces))

# sample: muestra SIN reemplazo
print(random.sample(range(10), 5))

# shuffle: baraja in-place una lista
L = [1, 2, 3, 4, 5]
random.shuffle(L)
print(L)

# uniform: flotantes en [a, b]
print(random.uniform(0,1))

# ---------------------------------------------------------------
# E) MÓDULO statistics: MEDIDAS SIMPLES
# ---------------------------------------------------------------
import statistics

data = [10, 20, 20, 30, 40, 40, 40]
print(statistics.mean(data))     # promedio
print(statistics.median(data)) # mediana

# ---------------------------------------------------------------
# F) MÓDULO string: CONSTANTES Y LIMPIEZA DE TEXTO
# ---------------------------------------------------------------
import string

print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

# Limpieza de una línea: quitar puntuación y pasar a minúsculas
line = "¡Hola, mundo! Programar es GENIAL: 100% diversión."
# Construimos una nueva cadena sin puntuación:
clean = ""
for ch in line:
    if ch not in string.punctuation and ch != "¡" and ch != "¿":
        clean = clean + ch
clean = clean.lower()
toks = clean.split()
print(toks)

# Contar frecuencias con diccionario:
freq = {}
for t in toks:
    if t in freq:
        freq[t] = freq[t] + 1
    else:
        freq[t] = 1
print(freq)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Normalizar y tokenizar texto usando 'string' y construir histograma con dict
import string
s = input("Texto: ")
cleaned = ""
for ch in s:
    if ch not in string.punctuation and ch != "¡" and ch != "¿":
        cleaned = cleaned + ch
toks = cleaned.lower().split()
hist = {}
for w in toks:
    if w in hist: hist[w] = hist[w] + 1
    else: hist[w] = 1
print(hist)

# Caso 2) Simulación de dados con 'random' y resumen con 'statistics'
import random, statistics
random.seed(2024)  # fija la semilla para reproducción
N = int(input("Tiros de dado: "))
rolls = []
for _ in range(N):
    rolls.append(random.randint(1,6))
print("mean:", statistics.mean(rolls))
print("median:", statistics.median(rolls))
print("multimode:", statistics.multimode(rolls))

# Caso 3) Geometría simple con 'math': hipotenusa y ángulos
import math
a = float(input("cateto a: "))
b = float(input("cateto b: "))
hyp = math.sqrt(a*a + b*b)
ang = math.degrees(math.atan2(b, a))  # ángulo en grados
print("hipotenusa:", hyp, "ángulo:", ang)

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización de soluciones probadas (funciones listas para usar).
# - Claridad: 'import math' comunica intención; menos código propio a mantener.
# - Consistencia y precisión: p.ej., 'statistics.mean' y 'math.isclose' evitan errores comunes.
#
# Desventajas / riesgos:
# - Mal uso de importaciones (espacios de nombres contaminados) puede causar choques de nombres.
# - Depender de funciones sin entender precondiciones (dominio de sqrt, modo único en statistics.mode).
#
# Buenas prácticas:
# - Prefiere 'import modulo' y usa el prefijo 'modulo.funcion' para legibilidad.
# - Documenta supuestos (rango de datos, dominios) y captura excepciones (ValueError, StatisticsError).
# - Para reproducibilidad con 'random', fija 'random.seed(...)' durante ejemplos y pruebas.
# - Activa una bandera DEBUG para imprimir valores intermedios si hace falta.