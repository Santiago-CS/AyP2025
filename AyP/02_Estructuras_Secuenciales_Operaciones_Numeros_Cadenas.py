# ===============================================================
# 2.- ESTRUCTURAS SECUENCIALES: OPERACIONES, NÚMEROS Y CADENAS

# ---------------------------------------------------------------
# B) TEORÍA: NÚMEROS, LITERALES Y OPERADORES ARITMÉTICOS
# ---------------------------------------------------------------
# TIPOS NUMÉRICOS EN ESTA SESIÓN
# - int  : enteros de precisión arbitraria (no hay overflow en Python por magnitud).
# - float: números en punto flotante (doble precisión IEEE-754).
#
# LITERALES
# - Enteros: 0, 1, 42, -7
# - Separador visual con guion bajo: 1_000_000 (equivale a 1000000)
# - Flotantes: 3.14, -0.5, 2.0, .5, 5., 1e3 (1000.0), 2.5e-3 (0.0025)
#
# OPERADORES ARITMÉTICOS
# +  suma
# -  resta (también negación unaria, p. ej., -x)
# *  multiplicación
# /  división real (siempre produce float)
# // división entera (floor division)
# %  módulo (residuo)
# ** potencia (exponenciación)
#
# OBSERVACIONES
# - / siempre devuelve float (ej. 5/2 -> 2.5)
# - // "piso": 5//2 -> 2, -5//2 -> -3 (redondea hacia abajo)
# - % cumple: a == (a//b)*b + (a % b) para b != 0
# - ** tiene mayor precedencia que * y /.
# - Cuidado con la precisión en float; 0.1 + 0.2 puede ser 0.30000000000000004.

# --- Código ilustrativo: literales y operaciones ---
a = 1_000_000      # int con separador visual
b = 250_000
c = 3.5e2          # 350.0
d = .75            # 0.75
e = 5.             # 5.0

print("a:", a, "| b:", b, "| c:", c, "| d:", d, "| e:", e)

# Aritmética básica
x = 10
y = 3
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)    # float
print("x // y =", x // y)  # división entera
print("x % y =", x % y)    # residuo
print("x ** y =", x ** y)  # potencia

# Identidad: a == (a//b)*b + (a % b)
num = 29
den = 5
print("Check identity:", num == (num // den) * den + (num % den))

# Precisión en float (simple demostración)
print("0.1 + 0.2 =", 0.1 + 0.2)

# ---------------------------------------------------------------
# C) TEORÍA: PRECEDENCIA Y ASOCIATIVIDAD
# ---------------------------------------------------------------
# (De mayor a menor prioridad en lo que usamos aquí)
# 1) **        (derecha a izquierda)
# 2) *, /, //, %
# 3) +, -
# - Los paréntesis alteran el orden y SIEMPRE son la mejor forma de dejar claro
#   qué se desea calcular primero.
# - Asociatividad:
#   - ** es derecha a izquierda: 2**3**2 = 2**(3**2) = 2**9 = 512
#   - *, /, //, %, +, - son izquierda a derecha.

# --- Código ilustrativo: precedencia y paréntesis ---
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)          # 512
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)      # 64

expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4
print("2 + 3 * 4 =", expr1)                  # 14
print("(2 + 3) * 4 =", expr2)                # 20

# ---------------------------------------------------------------
# D) TEORÍA: CONVERSIÓN DE TIPOS Y FUNCIONES NUMÉRICAS BÁSICAS
# ---------------------------------------------------------------
# CONVERSIÓN 
# - int("10")    -> 10
# - float("3.5") -> 3.5
# - str(42)      -> "42"
# - int(3.9)     -> 3     (trunca)
# - float(5)     -> 5.0
#
# FUNCIONES INTEGRADAS ÚTILES
# - abs(x)         : valor absoluto
# - round(x)       : redondeo al entero más cercano; .5 redondea al par más cercano (Banker's rounding)
# - round(x, n)    : redondeo con n decimales
# - pow(a, b)      : potencia (equivalente a a ** b)
# - min(x, y, ...) : mínimo
# - max(x, y, ...) : máximo

# --- Código ilustrativo: casting y funciones numéricas ---
print("int('15'):", int("15"))
print("float('2.75'):", float("2.75"))
print("str(123):", str(123))
print("int(3.99):", int(3.99))

print("abs(-7):", abs(-7))
print("round(2.5):", round(2.5))
print("round(3.5):", round(3.5))
print("round(3.141592, 2):", round(3.141592, 2))
print("pow(2, 10):", pow(2, 10))
print("min(4, 9, -2, 7):", min(4, 9, -2, 7))
print("max(4, 9, -2, 7):", max(4, 9, -2, 7))

# ---------------------------------------------------------------
# E) TEORÍA: CADENAS (STRINGS), OPERADORES Y MÉTODOS
# ---------------------------------------------------------------
# CADENAS (str)
# - Secuencias de caracteres inmutables.
# - Se pueden delimitar con comillas simples '...' o dobles "..." indistintamente.
# - Soportan escape de caracteres: \\n (salto de línea), \\t (tab), \\\\ (backslash), \\' y \\".
# - Se pueden escribir cadenas multilínea con triples comillas: ''' ... ''' o \"\"\" ... \"\"\"
#
# OPERACIONES BÁSICAS
# - Concatenación: "Hola" + " " + "Mundo"
# - Repetición: "ha" * 3  -> "hahaha"
# - Longitud: len("texto")
# - Acceso por índice:  s[0], s[1], ..., s[len(s)-1]
# - Índices negativos: s[-1] (último), s[-2], etc.
# - Rebanado (slicing): s[inicio:fin:paso]
#   * inicio incluido, fin excluido; cualquiera puede omitirse.
#   * Ejemplos: s[:3], s[3:], s[1:5], s[::-1] (inverso)
#
# MÉTODOS FRECUENTES 
# - s.upper(), s.lower(), s.title()
# - s.strip(), s.lstrip(), s.rstrip()
# - s.replace(old, new)
# - s.find(sub)      -> índice o -1 si no existe
# - s.startswith(pre), s.endswith(suf)
# - s.split(sep)     -> lista de partes (aún no profundizamos en listas)
# - 'sep'.join(iterable_de_cadenas)  -> une con separador
#
# FORMATO DE CADENAS
# - "Alumno: {} | Cal: {:.2f}".format(name, score)
# - f"Alumno: {name} | Cal: {score:.2f}"
# - Alineación/ancho: {:>10}, {:<10}, {:^10}, relleno con ceros: {:06d}
# - Separador de miles: format(1000000, ',')  -> '1,000,000'
#
# INMUTABILIDAD
# - s[0] = 'H'  -> ERROR (no se puede asignar por índice).
# - Para "modificar", se construye una nueva cadena.
'''
Hola buenas tardes como estamos es la clase de AyP O2025
'''
# --- Código ilustrativo: cadenas ---
s = "  Python para todos  "
print("s ->", repr(s))
print("len(s) ->", len(s))

# Acceso, Indexación     y slicing
t = "algoritmo"
print("t[0] ->", t[0])
print("t[-1] ->", t[-1])
print("t[0:4] ->", t[0:4])   # 'algo'
print("t[:4] ->", t[:4])
print("t[4:] ->", t[4:])
print("t[::-1] ->", t[::-1]) # reversa

# Métodos de limpieza y transformación
print("strip ->", s.strip())
print("upper ->", t.upper())
print("title ->", "introduccion a python".title())
print("replace ->", t.replace("algo", "meta"))

# Búsqueda y comprobaciones
u = "programacion"
print("u.find('grama') ->", u.find("grama"))
print("u.startswith('pro') ->", u.startswith("pro"))
print("u.endswith('cion') ->", u.endswith("cion"))

# split y join (solo demostración de resultado)
name_line = "Luis,24,Guadalajara"
parts = name_line.split(",")
print("split(',',) ->", parts)    # se imprime una lista; aún no se estudian a fondo
print("join ->", " | ".join(["A", "B", "C"]))

# Formato
student = "Luis"
score = 9.3571
print("format() -> Alumno: {} | Cal: {:.2f}".format(student, score))
print(f"f-string -> Alumno: {student} | Cal: {score:.2f}")
print("Ancho y alineación -> |{:>10}|{:<10}|{:^10}|".format("der", "izq", "centro"))
print("Ceros a la izquierda -> {:06d}".format(42))
print("Miles ->", format(1_234_567, ","))

# ---------------------------------------------------------------
# F) CASOS DE USO (SECUENCIALES)
# ---------------------------------------------------------------

# Caso 1) Mini calculadora secuencial (solo operaciones)
a = float(input("A: "))
b = float(input("B: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Producto:", a * b)
print("División real:", a / b)
print("División entera:", a // b)
print("Residuo:", a % b)
print("Potencia A**B:", a ** b)

# Caso 2) Formateo de recibo (cadenas + números)
concept = input("Concepto: ")
qty = int(input("Cantidad: "))
price = float(input("Precio unitario: "))
total = qty * price
print("----- RECIBO -----")
print(f"Concepto: {concept}")
print("Cantidad: {:>10d}".format(qty))
print("Precio:   ${:>10.2f}".format(price))
print("-------------------")
print("TOTAL:    ${:>10.2f}".format(total))

# Caso 3) Conversión de unidades (temperaturas)
c = float(input("Temperatura en °C: "))
f = c * 9/5 + 32
k = c + 273.15
print("°F:", round(f, 2), "| K:", round(k, 2))

# Caso 4) Plantilla de reporte con padding
course = input("Curso: ")
teacher = input("Profesor: ")
group = input("Grupo: ")
print("----- REPORTE -----")
print("Curso   : {:<20}".format(course))
print("Profesor: {:<20}".format(teacher))
print("Grupo   : {:<20}".format(group))

# ---------------------------------------------------------------
# G) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Operadores aritméticos y de cadenas permiten construir soluciones sin control de flujo.
# - Formateo de cadenas mejora la presentación de resultados.
# - Separadores en literales facilitan la lectura (1_000_000).
#
# Desventajas / riesgos:
# - Precisión en float: pequeñas diferencias por representación binaria.
# - round() usa redondeo al par en .5, lo cual puede sorprender a principiantes.
# - Inmutabilidad de cadenas: "modificar" requiere crear una nueva cadena.
#
# Buenas prácticas:
# - Usar paréntesis para dejar clara la intención en expresiones complejas.
# - Mantener nombres descriptivos y consistentes.
# - Al formatear dinero, mostrar 2 decimales y alinear columnas.