# 13.- FUNCIONES (I): MÓDULOS Y FUNCIONES. ESPECIFICACIÓN E IMPLEMENTACIÓN.
# B) TEORÍA: FUNCIÓN (ESPECIFICACIÓN VS IMPLEMENTACIÓN)
# ---------------------------------------------------------------
# FUNCIÓN: bloque reutilizable que recibe argumentos, realiza un procesamiento y
# opcionalmente devuelve un resultado con 'return'.
#
# ESPECIFICACIÓN (qué debe cumplir): nombre, parámetros, qué retorna, precondiciones,
# postcondiciones y descripción en español.
#
# IMPLEMENTACIÓN (cómo lo cumple): código dentro del cuerpo 'def ...:'.
#
# Estructura general:
#   def nombre(par1, par2):
#       \"\"\"Descripción breve.
#       Parámetros:
#           par1: tipo/rol esperado.
#           par2: tipo/rol esperado.
#       Retorna:
#           descripción del valor de retorno (o None si no retorna).
#       Precondiciones/Postcondiciones (si aplica).
#       \"\"\"
#       # cuerpo (usando solo lo visto)
#       # ...
#       return resultado  # o no retorna (retorno implícito None)
#
# Diferencia PRINT vs RETURN:
# - print muestra en pantalla; return entrega el valor para seguir usándolo en otro lugar.
# - Una función sin return explícito retorna None.
#
# Ejemplo simple:
def suma(a, b): #se hace una funcion y regresa a+b
    '''Suma dos números y retorna el resultado.'''
    return a + b

x = suma(10, 5)        # llamada
print("add(10,5) ->", x)  # 15

## Ejercicio 5 - crear una funcion para contar digitos en cadena
def suma_digitos(cadena):
    count = 0
    numero = "0123456789"
    for i in cadena:
        if i in numero:
            count += 1
    return count

suma_digitos("Hola buenos días a mis 19 alumnos sobrevivientes")

#CALCULADORA PARA CANDADO
def candado_examen(c1,c2,c3, c4, c5, c6, c7):
    suma = c1 + c2 + c3 + c4 + c5 + c6 + c7 
    promedio = suma / 7
    if c1 + c2 + c3 + c4 + c5 + c6 + c7 < 420:
        return "No pasa el candado", suma , promedio
    else:
        return "Si pasa el candado", suma , promedio

candado_examen(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))
##

# ---------------------------------------------------------------
# C) MÓDULOS: IMPORTACIÓN Y ESPACIOS DE NOMBRES
# ---------------------------------------------------------------
# Un módulo es un archivo con definiciones (funciones, constantes, etc.). Para usarlo:
#   import nombre_modulo
#   from nombre_modulo import nombre_objeto
#   import nombre_modulo as alias
#
# Demostración con el módulo estándar 'math' (operaciones numéricas básicas):
import math
print(math.pi)
print(math.sqrt(25))
print(math.floor(3.7))
print(math.ceil(3.1))    #El profe recomienda mas el uso de este para no crear confusiones con las variables

# También podemos importar un nombre específico:
from math import sqrt, ceil, floor, pi
print(sqrt(81))
pi
#Un apodo O usar un alias para el módulo:
import math as m
print(m.ceil(2.1))

# Nota pedagógica: por claridad en cursos iniciales, preferimos 'import math' y luego 'math.algo'.

# ---------------------------------------------------------------
# D) PARÁMETROS: POSICIONALES Y POR PALABRA CLAVE (BÁSICO)
# ---------------------------------------------------------------
# En Python, al llamar una función, podemos pasar argumentos por posición o nombrarlos.

def area_rectangulo(width, height):
    '''Retorna el área de un rectángulo width x height (ambos >= 0).'''
    if width < 0 or height < 0:
        return 0
    return width * height

# Llamadas por posición:
print(area_rectangulo(3, 4))

# Llamadas por palabra clave (keyword arguments):
print(area_rectangulo(height=4, width=3))

# Mezcla (posicionales primero, luego keywords):
print(area_rectangulo(5, height=2))

# ---------------------------------------------------------------
# E) ALCANCE: LOCALES VS. GLOBALES (Y PRECAUCIONES)
# ---------------------------------------------------------------
# Variables definidas dentro de una función son LOCALES a esa función.
# Variables definidas fuera pertenecen al ámbito GLOBAL del módulo.
# Evitar depender de globales salvo necesidad; pasar datos por parámetros es más claro.

DEBUG = False  # bandera global de depuración

def suma_1_a_todos(L):
    '''Suma 1 a cada entero de la LISTA L y retorna una NUEVA lista.'''
    if DEBUG:
        print("[DBG] original L:", L)
    R = []
    for x in L:
        R.append(x + 1)
    if DEBUG:
        print("[DBG] result R:", R)
    return R

data = [1, 2, 3]
print(suma_1_a_todos(data))
print("after call, data still:", data)  # data NO se modificó (retornamos copia)

# ---------------------------------------------------------------
# F) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Validación de entrada con función (retorna entero en [a..b] o None)
def read_int_in_range(a, b):
    '''Lee un entero usando input(); retorna el valor si está en [a..b], o None en caso contrario.'''
    raw = input("Enter int ["+str(a)+".."+str(b)+"]: ")
    try:
        n = int(raw)
        if a <= n <= b:
            return n
        else:
            print("Out of range")
            return None
    except ValueError:
        print("Not an integer")
        return None

v = read_int_in_range(10, 20)
print("read_int_in_range ->", v)

# Caso 2) Resumen de lista: suma, promedio, min, max (retorno múltiple con tupla)
def list_summary(nums):
    '''Recibe una lista de números y retorna (suma, promedio, min, max).
    Si la lista está vacía, retorna (0, None, None, None).'''
    
    if len(nums) == 0:
        return (0, None, None, None)
    s = 0.0
    mn = nums[0]; mx = nums[0]
    for x in nums:
        s = s + x
        if x < mn: mn = x
        if x > mx: mx = x
    avg = s / len(nums)
    return (s, avg, mn, mx)

print("list_summary demo:", list_summary([3, 7, 2, 9]))

# ---------------------------------------------------------------
# G) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización, claridad, pruebas más fáciles, depuración localizada.
# - Encapsulan detalles: cambias la implementación sin tocar el resto del programa.
#
# Desventajas/riesgos en principiantes:
# - Exceso de dependencia de variables globales puede generar errores sutiles.
# - Mala especificación (sin aclarar pre/post) crea confusión en el uso.
#
# Buenas prácticas:
# - Escribe una ESPECIFICACIÓN clara (docstring) antes de implementar.
# - Prefiere retornar valores a imprimir dentro de la función, salvo funciones “procedimiento”.
# - Diseña funciones pequeñas y con responsabilidad única.
# - Agrega trazas con bandera DEBUG cuando algo no cuadre.