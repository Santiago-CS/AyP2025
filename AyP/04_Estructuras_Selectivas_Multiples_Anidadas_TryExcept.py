 # ===============================================================
# 4.- ESTRUCTURAS SELECTIVAS: MÚLTIPLES, ANIDADAS, TRY-EXCEPT

# ---------------------------------------------------------------
# B) TEORÍA: IF-ELIF-ELSE (SELECCIÓN MÚLTIPLE)
# ---------------------------------------------------------------
# Sintaxis general:
#   if condicion1:
#       # bloque 1
#   elif condicion2:
#       # bloque 2
#   elif condicion3:
#       # bloque 3
#   else:
#       # bloque por defecto (opcional)
#
# Notas:
# - Se evalúan de arriba hacia abajo. La primera condición True ejecuta su bloque
#   y las demás se omiten.
# - El else final es opcional, pero útil como “caso por defecto”.
# - Usar paréntesis y condiciones claras, evitando expresiones enrevesadas.

# --- Código ilustrativo: mapeo de calificación numérica a letra ---
# Entrada: grade (0-100). Salida: A, B, C, D, F
grade = 87
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# ---------------------------------------------------------------
# C) TEORÍA: IF ANIDADOS (DECISIONES DENTRO DE DECISIONES)
# ---------------------------------------------------------------
# Patrón común:
#   if condicion_externa:
#       # ...
#       if condicion_interna:
#           # ...
#       else:
#           # ...
#   else:
#       # ...
#
# ¿Cuándo anidar?
# - Cuando una comprobación solo tiene sentido si otra ya se cumplió.
# - Útil para validar paso a paso: primero rango/forma, luego detalle.
# Recomendación: no anidar demasiado (dificulta la lectura). Prefiere elif
# cuando las condiciones son mutuamente excluyentes y “paralelas”.

# --- Código ilustrativo: validación de usuario con pasos ---
username = "admin"
pwd = "XYZ"
if username == "admin":
    if pwd == "XYZ":
        print("Welcome admin")
    else:
        print("Wrong password")
else:
    print("Unknown user")

# ---------------------------------------------------------------
# D) TEORÍA: TRY-EXCEPT (MANEJO BÁSICO DE ERRORES)
# ---------------------------------------------------------------
# ¿Por qué? input() devuelve TEXTO y las operaciones pueden fallar (ej. int("abc")).
# try-except evita que el programa “truene” y permite responder con un mensaje claro.
#
# Patrón básico:
#   try:
#       # código que puede fallar
#   except TipoDeError:
#       # qué hacer si ocurre ese error
#
# Variantes útiles:
#   - Múltiples except (uno por tipo de error frecuente).
#   - else: se ejecuta SOLO si no hubo excepción en try.
#   - finally: se ejecuta SIEMPRE (haya o no excepción).
#
# Errores comunes en esta sesión:
#   - ValueError: al convertir texto a número (int/float).
#   - ZeroDivisionError: al dividir entre 0.
#   - IndexError: indexar fuera de rango (con cadenas, si se accede a s[pos] inválida).
#   [inicio:fin:paso]
# Importante: sin ciclos, si ocurre error no re-pedimos datos; solo informamos.

# --- Código ilustrativo: conversión y división seguras ---
# 1) Conversión a int con captura de ValueError
text = "123x"
try:
    n = int(text)
    print("Parsed:", n)
except ValueError:
    print("Error: invalid integer literal")

# 2) División con captura de ZeroDivisionError
a, b = 10, 0
try:
    print("Division:", a / b)
except ZeroDivisionError:
    print("Error: division by zero")

# 3) Uso de else/finally
raw = "45"
try:
    x = int(raw)
except ValueError:
    print("Not an integer")
else:
    print("OK, x =", x)
finally:
    print("Done attempt")

# ---------------------------------------------------------------
# E) CASOS DE USO  
# ---------------------------------------------------------------

# Caso 1) Clasificador de temperatura del agua
t = float(input("Temp (C): "))
if t <= 0.0:
    print("Solid (ice)")
elif t < 100.0:
    print("Liquid")
else:
    print("Gas (vapor)")

# Caso 2) Registro con validación y try-except (edad numérica)
name = input("Name: ")
age_str = input("Age: ")
try:
    age = int(age_str)
    if age >= 18:
        print(f"{name} is adult")
    else:
        print(f"{name} is minor")
except ValueError:
    print("Error: age must be an integer")

# Caso 3) Cálculo de tarifa según tramo
usage = float(input("kWh used: "))
if usage < 150:
    rate = 0.85
elif usage < 300:
    rate = 1.05
else:
    rate = 1.25
total = usage * rate
print("Total: ${:.2f}".format(total))

# Caso 4) Verificación de correo del dominio permitido (anidado)
email = input("Email: ").strip()
if "@" in email:
    if email.lower().endswith("@uni.mx"):
        print("Allowed")
    else:
        print("Domain not allowed")
else:
    print("Invalid email (missing @)")

# ---------------------------------------------------------------
# F) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - if-elif-else expresa de forma clara decisiones con múltiples rutas.
# - if anidado permite validar por etapas.
# - try-except evita caídas ante entradas erróneas y mejora la experiencia del usuario.
#
# Desventajas / riesgos:
# - Anidamientos profundos dificultan la lectura (evitarlos).
# - Olvidar casos en elif deja rutas sin cubrir (agregar else por defecto si aplica).
# - Atrapar excepciones demasiado genéricas puede ocultar errores reales.
#
# Buenas prácticas:
# - Ordenar elif del caso más específico al más general.
# - Usar nombres claros y normalizar entradas de texto (.strip(), .lower()).
# - En try-except, capturar solo el error esperado (p.ej., ValueError) y dar mensajes útiles.

# Ejercicio 24 - Comparación de textos (case-insensitive)
# Enunciado: Lee dos textos; si iguales ignorando mayúsculas y espacios -> 'Equal', si no 'Different'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

text_a = input("Dame un texto:")
text_b = input("Dame un texto:")

if text_a.strip().lower().replace(' ', '') == text_b.strip().lower().replace(' ', ''):
    print ("Iguales")
else:
    print("Diferentes")
    # ---------------------------------------------------------------
# Ejercicio 36 - Validación de formato 'ABC-123'
# Enunciado: Lee código; si 3 letras + guion + 3 dígitos -> 'Valid'; si no 'Invalid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

formato = input("Ingresa 3 letras + guion + 3 digitos: ").upper()

if len(formato) == 7 and formato[0:3].isalpha() and formato[3] == '-' and formato[4:].isdigit():
  print('Valid')
else:
  print('Invalid')


  entrada = input().upper()


entrada = "ACB-123"

if entrada[3] == "-":
    entrada = entrada.split("-")
    print(entrada)
    if entrada[0].isalpha() and entrada[1].isnumeric and len(entrada[0]) == 3 and len(entrada[1]) == 3:
        print("Valido")
    else:
        print("Invalido")
else:
    print("Invalido")
    
#Profe----------------------------------------------------------------------------------------------

codigo = input("Código: ").upper()

flag = False
if len(codigo) == 7:
    if ("A" <= codigo[0] <= "Z") and ("A" <= codigo[0] <= "Z") and ("A" <= codigo[0] <= "Z"):
        if codigo[3] == "-":
            if ("0" <= codigo[4] <="9") and ("0" <= codigo[5] <="9") and ("0" <= codigo[6] <="9"):
                flag = True

if flag:
    print("Valid")
else:
    print("Invalid")

#Del profe hasta aqui-----------------------------------------------------------------------------------