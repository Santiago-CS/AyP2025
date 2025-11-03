# --- 1. PARSEO (Leer la matriz sin librerías) ---
# (Esta parte es igual a la del ejercicio anterior,
# usa trucos para partir el string)
matriz = []
input_str = input() # Ej: "[[1,2,3],[4,5,6]]"

s_filas = input_str[1:-1] # Ej: "[1,2,3],[4,5,6]"

if s_filas: # Revisa que no sea una matriz vacía "[[]]" o "[]"
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        s_numeros = fila_str[1:-1] # "1,2,3"
        fila_numeros = []
        if s_numeros:
            lista_de_strings_num = s_numeros.split(',') # ['1','2','3']
            for s_num in lista_de_strings_num:
                fila_numeros.append(int(s_num))
        matriz.append(fila_numeros)

# ¡Listo! 'matriz' ahora es [[1, 2, 3], [4, 5, 6]]

# --- 2. LÓGICA ESPIRAL ---
resultado = []
if matriz: # Nos aseguramos que la matriz no esté vacía
    
    # Definimos los 4 bordes
    fila_inicio = 0
    fila_fin = len(matriz) - 1
    col_inicio = 0
    col_fin = len(matriz[0]) - 1

    # El ciclo se repite mientras los bordes no se crucen
    while fila_inicio <= fila_fin and col_inicio <= col_fin:
        
        # --- Paso 1: Ir a la Derecha ---
        # Recorre la fila de MÁS ARRIBA (fila_inicio)
        for i in range(col_inicio, col_fin + 1):
            resultado.append(matriz[fila_inicio][i])
        # "Encogemos" el borde de arriba
        fila_inicio += 1 

        # --- Paso 2: Bajar ---
        # Recorre la columna de MÁS A LA DERECHA (col_fin)
        for i in range(fila_inicio, fila_fin + 1):
            resultado.append(matriz[i][col_fin])
        # "Encogemos" el borde de la derecha
        col_fin -= 1

        # --- Paso 3: Ir a la Izquierda ---
        # Revisa si los bordes no se cruzaron (para filas de 1 alto)
        if fila_inicio <= fila_fin:
            # Recorre la fila de MÁS ABAJO (fila_fin) en REVERSA
            for i in range(col_fin, col_inicio - 1, -1):
                resultado.append(matriz[fila_fin][i])
            # "Encogemos" el borde de abajo
            fila_fin -= 1

        # --- Paso 4: Subir ---
        # Revisa si los bordes no se cruzaron (para filas de 1 ancho)
        if col_inicio <= col_fin:
            # Recorre la columna de MÁS A LA IZQUIERDA (col_inicio) en REVERSA
            for i in range(fila_fin, fila_inicio - 1, -1):
                resultado.append(matriz[i][col_inicio])
            # "Encogemos" el borde de la izquierda
            col_inicio += 1

# --- 3. IMPRESIÓN ---
# Imprime la lista final con el formato [1,2,3,6,5,4]
print(f"[{','.join(map(str, resultado))}]")