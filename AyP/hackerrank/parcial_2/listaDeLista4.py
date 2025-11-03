# --- 1. PARSEO (Leer la matriz sin librerías) ---
# (Usamos el mismo truco de "SEPARADOR" de problemas anteriores)
matriz = []
input_str = input() # Ej: "[[1,2,3],[4,5,6]]"

s_filas = input_str[1:-1] # Ej: "[1,2,3],[4,5,6]"

if s_filas:
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        s_numeros = fila_str[1:-1] # "1,2,3"
        fila_numeros = []
        if s_numeros:
            lista_de_strings_num = s_numeros.split(',') # ['1','2','3']
            for s_num in lista_de_strings_num:
                fila_numeros.append(int(s_num))
        
        # Maneja el caso de entrada "[[]]"
        elif fila_str == "[]":
            matriz.append([])
            continue
        
        if fila_numeros:
             matriz.append(fila_numeros)

# ¡Listo! 'matriz' ahora es [[1, 2, 3], [4, 5, 6]]

# --- 2. LÓGICA DE TRANSPOSICIÓN ---
matriz_transpuesta = []
if matriz and matriz[0]: # Nos aseguramos que la matriz no esté vacía
    
    num_filas = len(matriz) # 2
    num_cols = len(matriz[0]) # 3 (longitud de la primera fila)
    
    # El ciclo exterior (i) recorre las COLUMNAS originales (0, 1, 2)
    # Cada 'i' creará una NUEVA FILA
    for i in range(num_cols):
        nueva_fila = []
        
        # El ciclo interior (j) recorre las FILAS originales (0, 1)
        # Cada 'j' tomará el elemento de esa fila
        for j in range(num_filas):
            
            # Agrega el elemento [j][i]
            # 1a vuelta (i=0): añade matriz[0][0] (1), luego matriz[1][0] (4) -> [1,4]
            # 2a vuelta (i=1): añade matriz[0][1] (2), luego matriz[1][1] (5) -> [2,5]
            # 3a vuelta (i=2): añade matriz[0][2] (3), luego matriz[1][2] (6) -> [3,6]
            nueva_fila.append(matriz[j][i])
            
        matriz_transpuesta.append(nueva_fila)

# --- 3. IMPRESIÓN ---
# Recorre la matriz transpuesta
# Imprime cada fila en su propia línea
# (Basado en tu corrección anterior, esta es la forma correcta)
for fila in matriz_transpuesta:
    # Formato sin espacios [1,4] y un salto de línea
    print(f"[{','.join(map(str, fila))}]")