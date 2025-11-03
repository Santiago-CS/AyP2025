# --- 1. PARSEO (Leer la matriz sin librerías) ---
matriz = []
input_str = input() # Ej: "[[11,2],[4,5]]"

s_filas = input_str[1:-1] # Ej: "[11,2],[4,5]"

if s_filas: 
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        s_numeros = fila_str[1:-1] # "11,2"
        fila_numeros = []
        if s_numeros:
            lista_de_strings_num = s_numeros.split(',') # ['11','2']
            for s_num in lista_de_strings_num:
                fila_numeros.append(int(s_num))
        
        # Solo añade si la fila_numeros no está vacía 
        # (previene error con entradas como "[[]]")
        if fila_numeros:
             matriz.append(fila_numeros)

# ¡Listo! 'matriz' ahora es [[11, 2], [4, 5]]

# --- 2. LÓGICA DE DIAGONALES ---
suma_principal = 0
suma_secundaria = 0
n = 0

if matriz: # Nos aseguramos que la matriz no esté vacía
    # Como es cuadrada, n = número de filas
    n = len(matriz) 
    
    # Recorremos las filas de 0 a n-1
    for i in range(n):
        
        # Añadimos el elemento de la diagonal principal
        suma_principal += matriz[i][i]
        
        # Añadimos el elemento de la diagonal secundaria
        suma_secundaria += matriz[i][n - 1 - i]

# --- 3. IMPRESIÓN ---
# Calcula la diferencia
diferencia = suma_principal - suma_secundaria

# Imprime el valor absoluto
# abs() es una función básica de Python, no necesita librería
print(abs(diferencia))