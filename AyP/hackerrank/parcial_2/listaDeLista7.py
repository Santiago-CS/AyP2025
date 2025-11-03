def parsear_matriz(input_str):
    """
    Función auxiliar para convertir un string "[[1,2],[3,4]]"
    en una lista de listas [[1, 2], [3, 4]] sin usar librerías.
    """
    matriz = []
    # Quita los corchetes exteriores, ej: "[1,2],[3,4]"
    s_filas = input_str[1:-1]

    if not s_filas: # Maneja el caso de "[]"
        return matriz
    
    # Usa el truco del SEPARADOR
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        # Quita los corchetes de la fila, ej: "1,2"
        s_numeros = fila_str[1:-1]
        
        fila_numeros = []
        if s_numeros: # Revisa que la fila no esté vacía
            lista_de_strings_num = s_numeros.split(',') # ['1','2']
            for s_num in lista_de_strings_num:
                fila_numeros.append(int(s_num))
        
        matriz.append(fila_numeros)
    return matriz

# --- 1. PARSEO (Leer ambas matrices) ---
input_str_A = input()
input_str_B = input()

matriz_A = parsear_matriz(input_str_A)
matriz_B = parsear_matriz(input_str_B)

# --- 2. LÓGICA DE MULTIPLICACIÓN ---

matriz_C = [] # Aquí guardaremos el resultado

if matriz_A and matriz_B:
    # Obtener las dimensiones
    m = len(matriz_A)      # Filas de A
    n = len(matriz_A[0])   # Columnas de A
    p = len(matriz_B[0])   # Columnas de B
    
    # CICLO i: Recorre las FILAS de A (de 0 a m-1)
    for i in range(m):
        nueva_fila_resultado = []
        
        # CICLO j: Recorre las COLUMNAS de B (de 0 a p-1)
        for j in range(p):
            
            # Ahora calculamos el valor de la celda [i][j]
            suma_celda = 0
            
            # CICLO k: Recorre las COLUMNAS de A / FILAS de B (de 0 a n-1)
            # Este es el ciclo que hace el "producto punto"
            for k in range(n):
                suma_celda += matriz_A[i][k] * matriz_B[k][j]
                
            # Guardamos el total de esa celda
            nueva_fila_resultado.append(suma_celda)
            
        # Guardamos la fila completa en la matriz resultado
        matriz_C.append(nueva_fila_resultado)

# --- 3. IMPRESIÓN ---
# Imprime cada fila de la matriz resultante en su propia línea
# y con el formato exacto [sin,espacios]
for fila in matriz_C:
    print(f"[{','.join(map(str, fila))}]")