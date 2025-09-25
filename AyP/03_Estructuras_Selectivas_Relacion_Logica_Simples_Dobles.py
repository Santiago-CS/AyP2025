
# ===============================================================
# 3.- ESTRUCTURAS SELECTIVAS: RELACIÓN, LÓGICA, SIMPLES Y DOBLES
#Ctrl + L = seleccionar toda la fila
#Shift + alt + flechas = duplica la seleccion
#ctrl + f3
#F8 go to next error
#Ctrl + ¡ = identa seleccion
#ctrl + shift + enter = linea arriba
#ALt + flechas (arriba y abajo) = Mueve la lin
# ---------------------------------------------------------------
# B) TEORÍA: VALORES BOOLEANOS Y "VERDAD" EN PYTHON
# ---------------------------------------------------------------
# - Un valor booleano es True o False.
# - Muchas expresiones devuelven booleanos, por ejemplo 3 < 5 -> True.
# - "Verdad" en Python (truthiness):
#   * Números: 0 es False; cualquier otro número es True.
#   * Cadenas: "" (vacía) es False; cualquier cadena no vacía es True.
# - Estas reglas permiten usar directamente números o cadenas en condiciones,
#   aunque por claridad conviene comparar explícitamente.
#
# Ejemplo (solo demostración):
#   if 5:        # True porque 5 != 0
#       print("Cinco es verdadero en contexto booleano")
#   if "hola":   # True porque no es cadena vacía
#       print("Cadena no vacía es verdadera")
#

# --- Código ilustrativo: truthiness explícita ---
value_num = 10
value_str = "python"
print("bool(10) ->", bool(value_num))
print("bool('python') ->", bool(value_str))
print("bool(0) ->", bool(0))
print("bool('') ->", bool(""))

# ---------------------------------------------------------------
# C) TEORÍA: OPERADORES DE RELACIÓN 
# ---------------------------------------------------------------
# ==  igualdad           (cuidado: para comparar, no confundir con = de asignación)
# !=  desigualdad
# <   menor que
# <=  menor o igual que
# >   mayor que
# >=  mayor o igual que
#
# COMPARACIÓN DE CADENAS
# - Es lexicográfica por código Unicode; "A" < "a" porque 'A' (65) < 'a' (97).
# - Suele ser buena idea normalizar con .lower() o .upper() antes de comparar.
#
# COMPARACIONES ENCADENADAS
# - Python permite: 1 < x < 10  (equivale a: 1 < x and x < 10)
# - Es útil para chequear intervalos sin escribir x dos veces.
#
# IGUALDAD vs IDENTIDAD
# - == compara valores; 'is' compara identidad de objeto .

# --- Código ilustrativo: relación ---
a = 7
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a <= 7:", a <= 7)
print("b > 5:", b > 5)
print("'Ana' == 'ana':", "Ana" == "ana")
print("'ana'.lower() == 'ana':", "ana".lower() == "ana")
x = 5
print("1 < x < 10:", 1 < x < 10)  # encadenada

# ---------------------------------------------------------------
# D) TEORÍA: OPERADORES LÓGICOS Y PRECEDENCIA
# ---------------------------------------------------------------
# and : True si ambas condiciones son True.
# or  : True si al menos una condición es True.
# not : invierte el valor booleano (not True -> False).
#
# PRECEDENCIA (de mayor a menor):
# 1) not
# 2) and
# 3) or
# - Usar paréntesis para dejar claro el orden es una buena práctica.
#
# CORTOCIRCUITO (short-circuit):
# - En (A and B): si A es False, no evalúa B.
# - En (A or B): si A es True, no evalúa B.

# --- Código ilustrativo: lógica ---
p = (10 > 3)          # True
q = ("py" in "python") # True
r = (0 == 1)          # False

print("p and q:", p and q)      # True
print("p or r:", p or r)        # True
print("not r:", not r)          # True

# Precedencia
print("not p or q:", not p or q)      # (not p) or q
print("not (p or q):", not (p or q))  # niega la disyunción

# ---------------------------------------------------------------
# E) TEORÍA: IF (SIMPLE) e IF-ELSE (DOBLE)
# ---------------------------------------------------------------
# IF (SIMPLE)
#   if condicion:
#       # bloque si True
#
# IF-ELSE (DOBLE)
#   if condicion:
#       # bloque si True
#   else:
#       # bloque si False
#

# --- Código ilustrativo: if simples y dobles ---
# Simple
temperature = 101.0
if temperature >= 100.0:  #if condicion:
    print("Boiling or above (>= 100°C)")    #lo que sucede si la condicion es true

# Doble
age = 17
if age >= 18:
    print("Adult:", age)
else:
    print("Minor:", age)

# Combinando lógica
total = 1200.0
has_coupon = "yes"
if (total >= 1000.0) and (has_coupon.lower() == "yes"):
    print("Discount applies")
else:
    print("No discount")

# ---------------------------------------------------------------
# F) CASOS DE USO (SECUENCIALES)
# ---------------------------------------------------------------

# Caso 1) Acceso sencillo por contraseña (igualdad de cadena, normalizando)
pwd = input("Password: ")
if pwd.strip() == "abc123":
    print("Access granted")
else:
    print("Access denied")

# Caso 2) Umbral de envío gratis (números + formateo)
subtotal = float(input("Subtotal: "))
if subtotal >= 799.0:
    print("Free shipping!")
else:
    shipping = 99.0
    print("Shipping cost: ${:.2f}".format(shipping))

# Caso 3) Verificación de rango (comparación encadenada)
x = float(input("Enter a value for x: "))
if 0.0 <= x <= 1.0:
    print("x in [0,1]")
else:
    print("x outside [0,1]")

# Caso 4) Comparación de cadenas sin sensibilidad a mayúsculas
city = input("City: ")
if city.strip().lower() == "guadalajara":
    print("Hola, tapatío/a.")
else:
    print("Bienvenido/a.")

# ---------------------------------------------------------------
# G) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - Permite controlar el flujo según condiciones del problema.
# - Combinación con operadores lógicos resuelve decisiones binarias complejas.
#
# Desventajas / riesgos:
# - Comparaciones con floats pueden verse afectadas por precisión (usar tolerancias).
# - Comparaciones de cadenas sensibles a mayúsculas y espacios (normalizar con strip/lower).
# - Código poco legible si se abusa de condiciones largas sin paréntesis.
#
# Buenas prácticas:
# - Expresar condiciones de forma clara y directa; usar paréntesis explicativos.
# - Normalizar entradas de texto: .strip(), .lower() antes de comparar.
# - Para floats, considerar tolerancia: abs(a-b) <= 1e-9 (según magnitud).