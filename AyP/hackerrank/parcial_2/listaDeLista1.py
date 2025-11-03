# --- 1. PARSEO (Leer la matriz sin librerías) ---
# (Esta parte es idéntica a la solución anterior)
matriz = []
input_str = input()
s_filas = input_str[1:-1]
s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
lista_filas_str = s_filas_separadas.split('SEPARADOR')
for fila_str in lista_filas_str:
    s_numeros = fila_str[1:-1]
    fila_numeros = []
    if s_numeros:
        lista_de_strings_num = s_numeros.split(',')
        for s_num in lista_de_strings_num:
            fila_numeros.append(int(s_num))
    matriz.append(fila_numeros)

# --- 2. LÓGICA DE ROTACIÓN (con Comprensión) ---
matriz_rotada = []
if matriz:
    num_filas = len(matriz) # <-- ¡Correcto! Con 4 espacios
    num_cols = len(matriz[0])

    # Esta es la traducción directa de los dos ciclos 'for' anidados:
    # [ (lo que queremos guardar) (ciclo exterior) (ciclo interior) ]
    #
    # Se lee: "Para cada 'i' en las columnas..."
    # "...crea una lista tomando 'matriz[j][i]'..."
    # "...para cada 'j' en las filas (en reversa)."
    matriz_rotada = [[matriz[j][i] for j in range(num_filas - 1, -1, -1)] for i in range(num_cols)]

# --- 3. IMPRESIÓN ---
if matriz:
    for fila in matriz_rotada:
        print(f"[{','.join(map(str, fila))}]")