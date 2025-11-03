# 12.- DATOS COMPUESTOS: DICCIONARIOS — CLAVES Y VALORES, PATRONES FUNDAMENTALES
# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UN DICCIONARIO?
# ---------------------------------------------------------------
# Definición:
# - Estructura de datos que asocia CLAVES con VALORES.
# - Sintaxis: {clave: valor, clave2: valor2, ...}
# - Claves: deben ser INMUTABLES (int, float, str, tupla de inmutables). Listas NO pueden ser claves.
# - Valores: pueden ser de cualquier tipo (números, cadenas, listas, tuplas, incluso otros diccionarios).
#
# Ejemplos:
empty = {}                      # diccionario vacío (¡no confundir con set!)
phone = {"Ana": "555-1234", "Luis": "555-9876"}    # str -> str
ages = {"Ana": 21, "Luis": 19, "Marta": 22}        # str -> int
coords = {(1,2): "A12", (3,4): "C34"}              # tupla -> str (clave compuesta)
print(empty, phone, ages, coords)
#
# Acceso por clave (KeyError si no existe):
print(phone["Ana"])
print(phone["Juan"])
#
# Inmutabilidad de la CLAVE vs mutabilidad del VALOR:
# - Claves no se pueden "cambiar": en realidad se elimina y se vuelve a insertar.
# - Si el valor es una lista, se puede mutar la lista SIN cambiar la clave:
catalog = {"A": [10, 20]}
catalog["A"].append(30)   # mutar el valor (lista) es válido
print(catalog)

# ---------------------------------------------------------------
# C) ACCESO, INSERCIÓN, ACTUALIZACIÓN Y ELIMINACIÓN
# ---------------------------------------------------------------
D = {}                   # crear vacío
D["x"] = 10              # inserción (si no existe crea, si existe actualiza)
print(D)
D["x"] = D["x"] + 5      # actualización
print(D)
#
# Lectura segura con verificación previa:
key = "y"
if key in D:
    print("D['y'] =", D["y"])
else:
    print("'y' not in D")
#
# Eliminación:
D["y"] = 99
print(D)
del D["y"]               # elimina la clave (KeyError si no está)
print(D)
#
# Eliminación segura con try-except:
try:
    del D["y"]
except KeyError:
    print("KeyError deleting 'y' (not present)")

# ---------------------------------------------------------------
# D) RECORRIDOS: CLAVES, VALORES, ÍTEMS
# ---------------------------------------------------------------
grades = {"Ana": 90, "Luis": 75, "Marta": 100}
# Por CLAVE (default):
s = 0
for name in grades:
    s = s + grades[name]
print(s)
# Explícito por claves:
for k in grades.keys():
    print(k)
# Por valores:
acc = 0
for v in grades.values():
    acc = acc + v
print(acc)
# Por ítems (par clave-valor):
for pair in grades.items():
    print(pair)       # par como tupla (k, v)
# Desempaquetando (tuplas) en el for:
total = 0
for k, v in grades.items():
    total = total + v
print(total)

# ---------------------------------------------------------------
# E) MÉTODOS BÁSICOS
# ---------------------------------------------------------------
data = {"a": 1, "b": 2}
print(len(data))                # cantidad de claves
print("a" in data)     # pertenencia por clave
#
# get: lectura con valor por defecto (no lanza KeyError)
print(data.get("c"))                # None si no está
print(data.get("c", 0))         # 0 por defecto
#
# pop: extrae valor y elimina la clave
data["x"] = 10
val = data.pop("x")                    # si no está -> KeyError
print(val, data)
# pop con valor por defecto (evita excepción)
val2 = data.pop("x", None)
print( val2, data)
#
# clear: vacía
tmp = {"k": 1}
tmp.clear()
print(tmp)
#
# keys, values, items devuelven VISTAS; podemos copiarlas a lista/tupla si se requiere
klist = list(data.keys())
vlist = list(data.values())
ilist = list(data.items())
print(klist, vlist, ilist)

# ---------------------------------------------------------------
# F) CONSTRUCCIÓN DESDE ENTRADAS
# ---------------------------------------------------------------
# F1) Cantidad fija de pares (for + range)
N = int(input("How many (key,value) pairs? "))
D = {}
for i in range(N):
    k = input("key: ")
    v = input("value: ")
    D[k] = v     # inserta o actualiza
print(D)
#
# F2) Centinela textual: leer 'k=v' hasta 'fin' (con validación sencilla)
D = {}
raw = input("k=v (or 'fin'): ")
while raw.strip().lower() != "fin":
    if "=" in raw:
        pos = raw.find("=")
        k = raw[:pos].strip()
        v = raw[pos+1:].strip()
        D[k] = v
    else:
        print("Formato inválido, use k=v")
    raw = input("k=v (or 'fin'): ")
print(D)

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Acceso directo por clave (muy eficiente conceptualmente).
# - Flexibilidad: valores pueden ser números, cadenas, listas, tuplas, etc.
# - Útiles para conteos, tablas de consulta y registros con campos nombrados.
#
# Desventajas / riesgos:
# - KeyError al acceder una clave inexistente (usa 'in' o get para prevenir).
# - Mutabilidad: cambiar un diccionario mientras se recorre puede llevar a confusión.
# - Claves deben ser inmutables; listas como claves NO son válidas.