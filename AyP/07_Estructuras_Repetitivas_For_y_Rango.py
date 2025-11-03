# 7.- ESTRUCTURAS REPETITIVAS: FOR Y RANGO
# ---------------------------------------------------------------
# B) TEORÍA: CICLO FOR — SINTAXIS Y FLUJO
# ---------------------------------------------------------------
# Sintaxis base:
#   for variable in iterable:
#       # bloque a repetir
#
# En esta sesión nuestros iterables serán:
#   - range(...)    -> genera secuencias de enteros
#   - cadenas (str) -> generan caracteres uno por uno
#
# Flujo:
# 1) Se obtiene el primer elemento del iterable y se asigna a 'variable'.
# 2) Se ejecuta el bloque.
# 3) Se repite con el siguiente elemento, hasta agotar el iterable.
#
# Importante:
# - El número de iteraciones queda determinado por el iterable (no por una condición booleana).
# - Si el iterable está vacío, el cuerpo no se ejecuta.

# --- Código ilustrativo: for básico con range ---
print("Contar de 0 a 4:")
for i in range(5):           # 0,1,2,3,4
    print(i)                #cuando solo pones un argumento, representa el fin del rango

print("Contar de 3 a 7:")
for x in range(3, 8):        # 3,4,5,6,7
    print(x)                #cuando pones dos argumentos, representa el inicio - fin del rango

print("Pares de 2 a 10 (paso 2):")
for n in range(2, 11, 2):    # 2,4,6,8,10
    print(n)                   #cuando pones tres argumentos, representa el inicio - fin y paso del rango

print("Descendiente de 5 a 1 (paso -1):")
for k in range(5, 0, -1):    # 5,4,3,2,1
    print(k)                 #con tres argumentos pero negativos

# ---------------------------------------------------------------
# C) TEORÍA: range() — FORMAS Y CASOS
# ---------------------------------------------------------------
# Formas:
# - range(stop)                -> 0, 1, ..., stop-1
# - range(start, stop)         -> start, start+1, ..., stop-1
# - range(start, stop, step)   -> start, start+step, ..., < stop
#
# Notas:
# - stop no se incluye (límite superior abierto).
# - step puede ser negativo: range(10, 0, -2) -> 10, 8, 6, 4, 2
# - Si con el step no se puede avanzar hacia el stop, el rango es VACÍO y el for no se ejecuta.
# - range() no crea listas (aún no vistas); es un objeto que genera valores bajo demanda.
#
# Comunes errores:
# - Confundir "n inclusive" con "stop exclusivo": para incluir N usa range(..., N+1).
# - Olvidar que el paso negativo exige start>stop.

# --- Código ilustrativo: variantes de range ---
print("range(0) -> no itera:")
for _ in range(0):
    print("no verás esto")

print("range(2, 2) -> vacío también:")
for _ in range(2, 2):
    print("tampoco verás esto")

print("range(10, 0, -3):")
for v in range(10, 0, -3):   # 10,7,4,1
    print(v)

# ---------------------------------------------------------------
# D) FOR SOBRE CADENAS: POR CARÁCTER Y POR ÍNDICE
# ---------------------------------------------------------------
# Dos enfoques principales:
# 1) Por carácter directo:
#       for ch in s:
#           # trabajar con ch
#    Útil para contar, buscar, filtrar.
#
# 2) Por índice (con range(len(s))):
#       for i in range(len(s)):
#           ch = s[i]
#    Útil cuando necesitas la posición (índice) explícita.
#
# Recordatorio: cadenas son inmutables; para "modificar" se construye una nueva.

# --- Código ilustrativo: cadenas ---
s = "Algoritmos"
count_vowels = 0
vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
for ch in s:
    if ch in vowels:
        count_vowels = count_vowels + 1
print(count_vowels)

# Índices
t = "Python"
for i in range(len(t)): #AQUI MANEJO EL CARACTER COMO UNA POSICION DENTRO DE LA PALABRA
    print(t[i])

for i in t: #AQUI MANEJO EL CARACTER DIRECTAMENTE
    print(i)
# ---------------------------------------------------------------
# E) FOR ANIDADOS: PATRONES Y TABLAS
# ---------------------------------------------------------------
# For anidado = un for dentro de otro. El externo controla "filas",
# el interno controla "columnas".
#
# Patrón de rectángulo de asteriscos (r filas x c columnas):
#   for i in range(r):
#       línea = ""
#       for j in range(c):
#           línea = línea + "*"
#       print(línea)
#
# Tabla (ej. multiplicar): dos for anidados para recorrer pares (i, j).

# --- Código ilustrativo: patrones y tabla ---
# Rectángulo 3x5
rows = 3
cols = 5
for i in range(rows):
    line = ""
    for j in range(cols):
        line = line + "*"
    print(line)

# Triángulo incremental (1..5)
for i in range(1, 6):
    print("#" * i)

# Tabla de multiplicar 1..3
for i in range(1, 4):
    for j in range(1, 6):
        print(str(i) + "x" + str(j) + "=" + str(i*j))
    print("---")

# ---------------------------------------------------------------
# F) CONTADORES Y ACUMULADORES CON FOR
# ---------------------------------------------------------------
# Contador: cuenta ocurrencias que cumplen una condición.
# Acumulador: suma/concatena resultados a través del ciclo.
#
# Esquema típico:
#   count = 0
#   for ...:
#       if condición:
#           count = count + 1
#
#   acc = 0
#   for ...:
#       acc = acc + valor

# --- Código ilustrativo: suma de pares y conteo de letras ---
# Suma de pares del 1 al 10
acc = 0
for n in range(1, 11):
    if n % 2 == 0:
        acc = acc + n
print(acc)

# Contar cuántas 'a' o 'A' hay en un texto
text = "Aula de Algoritmos"
count_a = 0
for ch in text:
    if ch == "a" or ch == "A":
        count_a = count_a + 1
print(count_a)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Suma de N reales (N leído por teclado)
N = int(input("How many values? "))
acc = 0.0
for i in range(N):
    x = float(input("Value " + str(i+1) + ": "))
    acc = acc + x
print("Sum:", acc)

# Caso 2) Impresión de rango con paso
start = int(input("Start: "))
stop = int(input("Stop (exclusive): "))
step = int(input("Step: "))
for v in range(start, stop, step):
    print(v)

# Caso 3) Procesamiento de cadena: contar dígitos, letras y otros
s = input("Text: ")
digits = 0
letters = 0
others = 0
for ch in s:
    if "0" <= ch <= "9":
        digits = digits + 1
    elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        letters = letters + 1
    else:
        others = others + 1
print("Digits:", digits, "Letters:", letters, "Others:", others)

# Caso 4) Tabla de multiplicar de un número hasta m
n = int(input("n: "))
m = int(input("m: "))
for i in range(1, m+1):
    print(n, "x", i, "=", n*i)

# ---------------------------------------------------------------
# H) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - For es ideal cuando se conoce de antemano el número de iteraciones
#   o cuando se recorre una secuencia (range o cadena).
# - Código compacto y claro comparado con while para contadores simples.
#
# Desventajas / riesgos:
# - Olvidar que range no incluye el límite superior.
# - Usar pasos incompatibles (p. ej., step positivo con start>stop) produce rangos vacíos.
#
# Buenas prácticas:
# - Nombrar claramente las variables de control (i, j) y las de estado (acc, count).
# - Comprobar casos límite: N=0, cadenas vacías, rangos vacíos.
# - Evitar dependencias externas en cada iteración (ej. no convertir repetidamente lo mismo).

# ---------------------------------------------------------------
# Ejercicio 10 - Contar dígitos
# Enunciado: Lee un texto y cuenta cuántos caracteres son dígitos ('0'..'9').
##
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
N = input()
count_words = 0
words = "0123456789"
for caracter in N:
    if caracter in words:
        count_words = count_words + 1
print(count_words)
# ---------------------------------------------------------------