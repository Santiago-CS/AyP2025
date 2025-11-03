# 11.- DATOS COMPUESTOS: TUPLAS — INMUTABILIDAD, EMPAQUETADO Y RECORRIDOS
# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UNA TUPLA?
# ---------------------------------------------------------------
# Definición:
# - TUPLA: colección ordenada, INDEXABLE e INMUTABLE (no se puede modificar un elemento).
# - Se escribe con paréntesis () y elementos separados por coma.
#
# Ejemplos:
t = (10, 20, 30)
print(t)
u = ("uno", "dos", "tres")
print(u)
mix = (1, "A", 2.5)  # posible, pero se recomienda homogeneidad cuando sea práctico
print(mix)
empty = ()           # tupla vacía
print(empty)
#
# Tupla de 1 elemento (¡requiere coma!):
one = (5,)           # si escribes (5) es solo el entero 5
print(one, type(one))
not_tuple = (5)
print(not_tuple, type(not_tuple))
#
# Inmutabilidad:
# - No puedes reasignar t[0] = 99 (TypeError).
t[0] = 99  

# ---------------------------------------------------------------
# C) ÍNDICES Y SLICES; CONCATENACIÓN (+) Y REPETICIÓN (*)
# ---------------------------------------------------------------
a = (5, 6, 7, 8, 9)
print(a[0], a[-1])
print(a[1:4])   # subtupla desde 1 hasta 3
print(a[:3])
print(a[3:])
print(a[:])     # copia superficial (nuevo objeto tupla)

# Operadores:
x = (1, 2)
y = (3, 4, 5)
print(x + y)     # concatenación
print(y * 2)     # repetición 

# ---------------------------------------------------------------
# D) RECORRIDOS CON FOR/WHILE; PERTENENCIA 'in'
# ---------------------------------------------------------------
t = (3, 7, 2, 9)
total = 0
for val in t:
    total = total + val
print(total)

total2 = 0
for i in range(len(t)):
    total2 = total2 + tupla[i]
print(total2)

i = 0
total3 = 0
while i < len(t):
    total3 = total3 + t[i]
    i = i + 1
print(total3)

# Pertenencia:
print(7 in t)
print(10 in t)

# ---------------------------------------------------------------
# E) MÉTODOS Y OPERACIONES DISPONIBLES
# ---------------------------------------------------------------
# len(t) -> longitud
# t.index(x) -> índice de la primera aparición de x (ValueError si no está)
# t.count(x) -> cuántas veces aparece x
# Conversión: list(t) para obtener lista mutable; tuple(L) para crear tupla desde lista
#
w = ("a", "b", "a", "c", "a")
print(len(w))
print(w.count("a"))
print(w.index("b"))
#
L = list(w)         # copia en lista
L[0] = "A"          # modifico la lista (no la tupla original)
print(L)
w2 = tuple(L)       # vuelvo a tupla
print(w2)
#
# join/split con tuplas de cadenas (permitido):
parts = ("hola", "mundo")
print(" ".join(parts))
line = "uno dos tres"
tok = tuple(line.split())  # tuple de tokens
print(tok)

# ---------------------------------------------------------------
# F) EMPAQUETADO Y DESEMPAQUETADO
# ---------------------------------------------------------------
# Empaquetado: se crea una tupla sin paréntesis usando comas.
p = 10, 20, 30
print(p, type(p))

# Desempaquetado múltiple:
a, b, c = p
print(a, b, c)

# Swap (intercambio) de variables usando tuplas:
x = 1; y = 2
x, y = y, x
print(x, y)

# Desempaquetado con * (estrella) para capturar "el resto":
t = (1, 2, 3, 4, 5, 6)
first, *middle, last = t
print(first, middle, last)
# Nota: middle es una LISTA (lo permite Python); puedes convertirla a tupla si lo necesitas:
middle_t = tuple(middle)
print(middle_t, type(middle_t))

# ---------------------------------------------------------------
# G) TUPLAS ANIDADAS Y TUPLAS CON LISTAS
# ---------------------------------------------------------------
# Tuplas anidadas:
T = ( (1,2), (3,4,5), (6,) )
print(T, T[1][2])

# Tupla con lista interna (la tupla es inmutable, pero la lista sí cambia):
U = (1, [10, 20], 3)
print(U)
U[1].append(99)    # válido: NO cambiamos la tupla, cambiamos la lista que contiene
print(U)
#
# Cuidado: U[0] = 100 -> TypeError (prohibido modificar posiciones de la tupla)