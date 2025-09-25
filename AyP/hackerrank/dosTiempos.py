# --- Lectura de los datos de entrada ---
# Tiempo 1
h1 = int(input())
m1 = int(input())
s1 = int(input())

# Tiempo 2
h2 = int(input())
m2 = int(input())
s2 = int(input())

# --- Lógica del programa ---

# 1. Convertir ambos tiempos a un total de segundos.
# 1 hora = 3600 segundos, 1 minuto = 60 segundos.
total_segundos1 = h1 * 3600 + m1 * 60 + s1
total_segundos2 = h2 * 3600 + m2 * 60 + s2

# 2. Sumar los totales para obtener el gran total en segundos.
gran_total_segundos = total_segundos1 + total_segundos2

# 3. Convertir el gran total de segundos de vuelta a formato H M S.
# Obtener las horas totales usando división entera.
H = gran_total_segundos // 3600

# Obtener los segundos que "sobran" después de quitar las horas.
segundos_restantes = gran_total_segundos % 3600

# De los segundos restantes, obtener los minutos totales.
M = segundos_restantes // 60

# De los segundos restantes, obtener los segundos finales.
S = segundos_restantes % 60

# --- Impresión del resultado ---
print(H, M, S)