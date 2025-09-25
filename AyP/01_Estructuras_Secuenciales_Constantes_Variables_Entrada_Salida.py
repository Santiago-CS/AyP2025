# ===============================================================
# 1.- ESTRUCTURAS SECUENCIALES: CONSTANTES Y VARIABLES, ENTRADA Y SALIDA
# ---------------------------------------------------------------
# B) TEORÍA: CONSTANTES, VARIABLES E IDENTIFICADORES
# ---------------------------------------------------------------
# ¿Qué es una VARIABLE?
# - Es un nombre (identificador) que REFERENCIA un valor en memoria.
# - En Python el tipeado es dinámico: el mismo nombre puede referenciar
#   a valores de diferente tipo en momentos distintos.
#
# ¿Qué es una CONSTANTE?
# - En Python no existen constantes "estrictas" a nivel de lenguaje.
# - Por CONVENCIÓN utilizamos nombres con MAYÚSCULAS y GUIONES_BAJOS
#   para indicar "no modificar este valor". Ejemplo: PI = 3.14159
# - Disciplina del equipo: respetar que las constantes no cambian.
#
# IDENTIFICADORES (nombres válidos para variables/constantes)
# - Pueden contener letras (A-z), dígitos (0-9) y guion bajo (_).
# - NO pueden empezar con dígito.
# - Son sensibles a mayúsculas/minúsculas: nombre != Nombre != NOMBRE
# - NO pueden ser palabras reservadas del lenguaje (keywords).

# TIPOS BÁSICOS EN ESTA SESIÓN
# - int   (enteros): 0, 1, -3, 42
# - float (reales):  3.14, -0.5, 2.0
# - str   (cadenas): "hola", 'Python', ""
# - bool  (booleanos): True, False
#
# OBSERVACIÓN SOBRE INMUTABILIDAD (ideas introductorias)
# - Las cadenas (str) son INMUTABLES: no se puede cambiar un carácter por índice.

# Asignación simple (variable -> valor)
course_name = "Algoritmos y Programación"   # str
credits = 6                                  # int
average_grade = 9.1                          # float
is_active = True                             # bool

# Mostrar valores y sus tipos
print("course_name:", course_name, "| type:", type(course_name))
print("credits:", credits, "| type:", type(credits))
print("average_grade:", average_grade, "| type:", type(average_grade))
print("is_active:", is_active, "| type:", type(is_active))

# Constante por convención (no se debe modificar)
PI = 3.14159
MAX_STUDENTS = 40
print("PI:", PI, "| MAX_STUDENTS:", MAX_STUDENTS)

# Identificadores válidos/ inválidos (solo comentarios):
# válido: user_name, _hidden_value, age2, TOTAL_SUM
# inválido: 2age (no puede empezar con dígito), user-name (guion NO permitido), class (keyword)

# Palabras reservadas (keywords): nombres que NO pueden usarse como identificadores.
# Las listamos solo para referencia visual.

import keyword
print("Python keywords:", keyword.kwlist)
print("Total keywords:", len(keyword.kwlist))

# ---------------------------------------------------------------
# C) TEORÍA: ENTRADA Y SALIDA (input/print)
# ---------------------------------------------------------------
# FUNCIÓN print(*objetos, sep=' ', end='\n')
# - Imprime los objetos separados por 'sep' y finaliza con 'end'.
# - Ejemplos de parámetros útiles:
#   - sep: cambia el separador entre objetos impresos.
#   - end: cambia el final de línea (por defecto es salto de línea).
# - Soporta diferentes formas de formateo: concatenación, format(), f-strings.
#
# FUNCIÓN input(prompt)
# - Muestra el mensaje 'prompt' y LEE una línea desde el teclado.
# - SIEMPRE retorna un str (cadena). Si se requieren números, hay que convertir.
#
# CONVERSIÓN DE TIPOS (CASTING):
# - int("10") -> 10
# - float("3.5") -> 3.5
# - str(10) -> "10"
# - bool(""), bool("hola")
#   Nota: bool('') es False, bool('0') es True (cualquier cadena no vacía -> True).
#
# FORMATEO DE SALIDA (básico en esta sesión)
# - Concatenación con + (requiere str en ambos lados).
# - print con múltiples argumentos separados por coma (automatiza espacios).
# - str.format("... {0} ... {1} ...".format(a,b))
# - f-strings: f"Hola {nombre}, edad {edad}"
#   (f-strings requieren Python 3.6+).

# --- Código ilustrativo: print ---
print("Hola", "mundo")                     # usa sep por defecto = " "
print("A", "B", "C", sep="-")              # sep cambia el separador
print("Sin salto al final...", end="")     # end="" evita salto de línea
print(" <- Continuación de la misma línea")

# Formatos:
student = "Luis"
age = 24
print("Alumno:", student, "| Edad:", age)                  # múltiple con coma
print("Alumno: " + student + " | Edad: " + str(age))       # concatenación
print("Alumno: {} | Edad: {}".format(student, age))        # format()
print(f"Alumno: {student} | Edad: {age}")                  # f-string (recomendado)

# --- Código ilustrativo: input ---
name = input("Ingresa tu nombre: ")
print("Hola,", name)

# Lectura y conversión básica
year_str = input("Ingresa un año (entero): ")
year = int(year_str)     # conversión str -> int
print("Año leído (int):", year, "| type:", type(year))

height_str = input("Ingresa tu estatura en metros (ej. 1.75): ")
height = float(height_str)  # conversión str -> float
print("Estatura:", height, "| type:", type(height))

# Advertencia: Si el usuario ingresa algo no convertible (ej. 'uno' en int) se lanzará

# ---------------------------------------------------------------
# D) CASOS DE USO 
# ---------------------------------------------------------------

# Caso 1) Ficha de registro simple (eco de datos)
full_name = input("Nombre completo: ")
student_id = input("Matrícula/ID: ")
degree = input("Programa académico (ej. 'Ing. Civil', 'Ing. en Nanotecnología'): ")
semester = input("Semestre (texto o número): ")
print("\n--- RESUMEN ---")
print(f"Nombre: {full_name}")
print(f"ID: {student_id}")
print(f"Programa: {degree}")
print(f"Semestre: {semester}")

# Caso 2) Tarjeta de presentación (formateo de salida)
first_name = input("Nombre: ")
last_name = input("Apellido: ")
email = input("Correo institucional: ")
print("\n----- TARJETA -----")
print(f"{last_name}, {first_name}")
print(email)

# Caso 3) Comprobante de inscripción (composición de cadenas)
curso = input("Curso: ")
grupo = input("Grupo: ")
aula = input("Aula/Laboratorio: ")
horario = input("Horario (ej. 'Lun-Mié 7:00-9:00'): ")
print("\n*** COMPROBANTE ***")
print("Curso:", curso, "| Grupo:", grupo, "| Aula:", aula, "| Horario:", horario)

# Caso 4) Eco numérico con conversión (sin operaciones avanzadas)
horas_str = input("Horas inscritas (entero): ")
horas = int(horas_str)
creditos_str = input("Créditos (entero): ")
creditos = int(creditos_str)
print("\nResumen numérico -> horas:", horas, ", créditos:", creditos)

# ---------------------------------------------------------------
# E) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas de las variables en programas secuenciales:
# - Facilitan almacenar y reutilizar valores (evitar "números mágicos").
# - Mejoran la legibilidad y el mantenimiento del código.
# - Permiten separar "entrada" de "cálculo" y "salida".
#
# Desventajas / riesgos comunes:
# - Nombres poco descriptivos generan confusión (evitar 'a', 'b', 'c' sin contexto).
# - Cambiar el tipo de una variable accidentalmente (por tipado dinámico) puede
#   causar errores lógicos. Mantener coherencia de tipos.
# - Con input(), TODO llega como str. Si se necesitan números, convertir explícitamente.
#
# Buenas prácticas:
# - Usar identificadores descriptivos y seguir PEP 8.
# - Definir "constantes" en UPPER_SNAKE_CASE al inicio del archivo si aplican.
# - Agrupar la lectura de datos (input) al principio, el "proceso" al centro
#   (se verá más en Sesión 2) y la presentación (print) al final.
# - Comentar el código teórico con claridad (como en este documento).