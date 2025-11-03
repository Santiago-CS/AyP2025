# 10.- DATOS COMPUESTOS: LISTAS (II) — PATRONES AVANZADOS, ANIDADAS Y COMPRENSIONES
# ---------------------------------------------------------------
# B) LISTAS ANIDADAS (MATRICES): CREACIÓN Y RECORRIDO
# ---------------------------------------------------------------
# Matriz 3x3 fija:
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print(M)
print(M[0][1])   

# Recorridos:
# - Por filas
s = 0
for row in M:
    for val in row:
        s = s + val
print(s)

# - Por índices (i, j) #ESTO VA A VENIR EN EL EXAMEN
total = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        total = total + M[i][j]
print(total)

# Construcción programática de matriz r x c con ceros
r = 3; c = 4
Z = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(0)
    Z.append(row)
print(Z)

# ---------------------------------------------------------------
# C) CONSTRUCCIÓN PROGRAMÁTICA: TABLAS Y PATRONES
# ---------------------------------------------------------------
# Tabla de multiplicar 1..r por 1..c (guardada en matriz T)
r = 3; c = 5
T = []
for i in range(1, r+1):
    row = []
    for j in range(1, c+1):
        row.append(i*j)
    T.append(row)
print(T)

# Patrón de tablero (caracteres)
n = 5
board = []
for i in range(n):
    row = []
    for j in range(n):
        if (i + j) % 2 == 0:
            row.append("#")
        else:
            row.append(".")
    board.append(row)
print( board)

# ---------------------------------------------------------------
# D) BÚSQUEDA, FILTRADO Y TRANSFORMACIÓN (SIN FUNCIONES)
# ---------------------------------------------------------------
# Búsqueda de un valor v en M: devuelve (i,j) de la primera aparición o (-1,-1)
v = 6
pi = -1; pj = -1
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == v and pi == -1:
            pi = i; pj = j
print(v, (pi, pj))

# Filtrar pares de una lista L en R (mantener orden)
L = [5, 2, 8, 7, 4, 9]
R = []
for x in L:
    if x % 2 == 0:
        R.append(x)
print(R)

# Transformar: sumar 1 a cada elemento de L en una NUEVA lista
L2 = []
for x in L:
    L2.append(x + 1)
print("L2:", L2)

# ---------------------------------------------------------------
# E) ORDENAMIENTOS BÁSICOS (MANUALES)
# ---------------------------------------------------------------
# Burbuja ascendente (bubble sort) sobre copia para no tocar original
A = [7, 3, 9, 1, 4]
B = A[:]  
n = len(B)
for i in range(n-1):
    for j in range(n-1-i):
        if B[j] > B[j+1]:
            tmp = B[j]
            B[j] = B[j+1]
            B[j+1] = tmp
print(B)

# Selección ascendente (selection sort)
C = A[:]
n = len(C)
for i in range(n-1):
    min_pos = i
    for j in range(i+1, n):
        if C[j] < C[min_pos]:
            min_pos = j
    # swap
    tmp = C[i]; C[i] = C[min_pos]; C[min_pos] = tmp
print(C)

# ---------------------------------------------------------------
# F) CONVERSIÓN TEXTO<->LISTA: SPLIT Y JOIN
# ---------------------------------------------------------------
# split: separa una cadena en lista por separador (por defecto, espacios)
line = "uno dos   tres"
parts = line.split()  # maneja espacios múltiples
print(parts)

csv = "a,b,c,,d"
parts2 = csv.split(",")  # separador explícito
print(parts2)

# join: une elementos de una lista de strings con un separador
joined = "-".join(["A", "B", "C"])
print(joined)

# ---------------------------------------------------------------
# G) COMPRENSIONES DE LISTAS (BÁSICAS)
# ---------------------------------------------------------------
# Regla en esta sesión: SOLO una cláusula for y un filtro opcional "if".
# Sin 'if-else' dentro de la expresión y sin anidar comprensiones.
#
# Ejemplos:
nums = [1,2,3,4,5,6]
# cuadrados de números pares
squares_even = [x*x for x in nums if x % 2 == 0]
print(squares_even)

## esto de abajo es lo mismo que lo de aqui arriba ##
squares = []
for x in nums:
    if x % 2 == 0:
        squares.append(x**2)
##############################################################
# longitudes de palabras con 3+ letras
words = ["sol", "luz", "programa", "if", "for"]
lengths = [len(w) for w in words if len(w) >= 3]
print(lengths)

# ---------------------------------------------------------------
# H) FUNCIÓN MAP USANDO LAMBDA
# ---------------------------------------------------------------
nums = [1,2,3,4,5,6]
cubos = list(map(lambda x: x**3, nums))
print(cubos)

nums = ["1","2","3","4","5","6"]
enteros = list(map(lambda x: int(x), nums))
print(enteros)

