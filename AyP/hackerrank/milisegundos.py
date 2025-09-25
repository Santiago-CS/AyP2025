# --- Constantes de conversión ---
#definicion de  estos valores para que el código sea más legible.
MS_EN_SEGUNDO = 1000
MS_EN_MINUTO = MS_EN_SEGUNDO * 60      # 60,000
MS_EN_HORA = MS_EN_MINUTO * 60         # 3,600,000
MS_EN_DIA = MS_EN_HORA * 24            # 86,400,000

# --- Lectura de la entrada ---
total_ms = int(input())

# --- Lógica de Descomposición ---
# 1. Calcular los DÍAS y el resto
dias = total_ms // MS_EN_DIA
ms_restantes = total_ms % MS_EN_DIA

# 2. Del resto, calcular las HORAS y el nuevo resto
horas = ms_restantes // MS_EN_HORA
ms_restantes = ms_restantes % MS_EN_HORA # Actualizar el resto

# 3. Del nuevo resto, calcular los MINUTOS y el nuevo resto
minutos = ms_restantes // MS_EN_MINUTO
ms_restantes = ms_restantes % MS_EN_MINUTO # Actualizar de nuevo

# 4. Del último resto, calcular los SEGUNDOS
segundos = ms_restantes // MS_EN_SEGUNDO
milisegundos = ms_restantes % MS_EN_SEGUNDO # Lo que sobra al final son los milisegundos

# --- Impresión con Formato ---
# Usamos f-strings para formatear la salida como se pide (D HH:MM:SS.mmm)
# :02d -> Formatea un entero para que tenga 2 dígitos, rellenando con un 0 a la izquierda si es necesario.
# :03d -> Lo mismo, pero para 3 dígitos.
print(f"{dias} {horas:02d}:{minutos:02d}:{segundos:02d}.{milisegundos:03d}")