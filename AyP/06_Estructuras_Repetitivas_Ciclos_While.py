# ===============================================================
# 6.- ESTRUCTURAS REPETITIVAS: CICLOS WHILE
# ---------------------------------------------------------------
# B) TEORÍA: WHILE (PRE-TEST), FLUJO Y TERMINACIÓN
# ---------------------------------------------------------------
# Sintaxis básica:
#   while condicion:
#       # bloque que se repite mientras la condición sea True
#
# Ideas clave:
# - "Pre-test": la condición se evalúa ANTES de cada iteración.
# - Si la condición es False desde el inicio, el cuerpo no se ejecuta nunca.
# - Para TERMINAR el bucle, en algún punto debe volver False la condición.
# - Para ello, normalmente ACTUALIZAMOS variables dentro del cuerpo.
#
# Pseudocódigo típico (contador):
#   i = 1                     # inicialización
#   while i <= N:             # condición
#       # trabajo
#       i = i + 1             # actualización
#
# Peligro común: bucle INFINITO si olvidamos la actualización o si la condición
# nunca cambia a False. Para evitarlo, analiza la condición y su actualización.
#
# Patrón con CENTINELA:
#   leer valor
#   while valor != 'fin':
#       procesar valor
#       leer valor
#
# En esta sesión NO usamos break/continue; ajusta la condición/actualización.

# ---------------------------------------------------------------
# C) PATRONES CLÁSICOS CON WHILE
# ---------------------------------------------------------------

# Patrón C1) Contador simple: imprimir 1..N (N conocido)

N = 5
i = 1
while i <= N:
    print("i =", i)
    i = i + 1  # actualización obligatoria

# Patrón C2) Acumulador: suma de 1..N (N conocido)

N = 5
i = 1
total = 0
while i <= N:
    total = total + i
    i = i + 1
print("Sum 1..N:", total)

# Patrón C3) Centinela textual: leer hasta 'fin' (sin listas)

print("Enter values, 'fin' to stop:")  # (Ejemplo demostrativo)
acc = 0.0
count = 0
val = input("Value (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        acc = acc + x
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    if count == 1:
        val = "3"
    elif count == 2:
        val = "fin"
    else:
        val = "fin"
if count == 0:
    print("No numbers")
else:
    print("Sum:", acc, "| Avg:", acc / count)

# ---------------------------------------------------------------
# D) VALIDACIÓN DE ENTRADAS CON WHILE Y TRY-EXCEPT (sin break/continue)
# ---------------------------------------------------------------
# Objetivo: asegurar que un dato cumpla un formato o rango antes de seguir.
#
# Patrón: bandera de validez
#   valid = False
#   while not valid:
#       raw = input(...)
#       try:
#           x = conversión(raw)
#           # si adicionalmente se requiere rango:
#           if condicion_de_rango:
#               valid = True
#           else:
#               print("Fuera de rango, intenta otra vez.")
#       except ValueError:
#           print("Formato inválido, intenta otra vez.")
#
# Nota: sin break/continue, la bandera controla la permanencia en el bucle.

# --- Ejemplo: leer un entero entre 1 y 5 ---
valid = False
while not valid:
    raw = input("Enter an integer [1..5]: ")
    try:
        n = int(raw)
        if 1 <= n <= 5:
            valid = True
        else:
            print("Out of range.")
    except ValueError:
        print("Not an integer.")
print("Accepted:", n)

# ---------------------------------------------------------------
# E) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Sumatoria de N reales
# (Lee N y luego N valores, acumulando la suma)
N_raw = input("How many values? ")
try:
    N = int(N_raw)
    i = 1
    acc = 0.0
    while i <= N:
        x = float(input("Value " + str(i) + ": "))
        acc = acc + x
        i = i + 1
    print("Sum:", acc)
except ValueError:
    print("Invalid N")

# Caso 2) Promedio con centinela 'fin'
acc = 0.0
count = 0
val = input("Value (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        acc = acc + x
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'fin'): ")
if count == 0:
    print("No numbers")
else:
    print("Sum:", acc, "| Avg:", acc / count)

# Caso 3) Menú sencillo (sin break/continue)
option = ""
while option != "4":
    print("\nMENU")
    print("1) Greet")
    print("2) Double a number")
    print("3) Square a number")
    print("4) Exit")
    option = input("Choose: ").strip()
    if option == "1":
        name = input("Name: ")
        print("Hello,", name)
    elif option == "2":
        try:
            x = float(input("Number: "))
            print("Double:", 2*x)
        except ValueError:
            print("Invalid number")
    elif option == "3":
        try:
            x = float(input("Number: "))
            print("Square:", x*x)
        except ValueError:
            print("Invalid number")
    elif option == "4":
        print("Bye!")
    else:
        print("Invalid option")

# ---------------------------------------------------------------
# F) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - while es flexible: útil cuando el número de iteraciones no es conocido.
# - Trabaja muy bien con centinelas y validación de entradas.
#
# Desventajas / riesgos:
# - Fácil crear bucles infinitos si se olvida actualizar la condición.
# - La lógica puede volverse confusa si la condición no es clara.
#
# Buenas prácticas:
# - Antes de codificar, redacta la CONDICIÓN de continuación en palabras.
# - Ubica la INICIALIZACIÓN antes del while y la ACTUALIZACIÓN dentro del cuerpo.
# - Prefiere banderas (valid = False) para control de repetición en validación.
# - Usa mensajes de error claros en try-except para ayudar al usuario.