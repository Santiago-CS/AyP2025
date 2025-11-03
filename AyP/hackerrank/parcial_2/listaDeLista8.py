def parsear_matriz(input_str):
    """
    Función auxiliar para convertir un string "[[1,2],[3,4]]"
    en una lista de listas [[1, 2], [3, 4]] sin usar librerías.
    """
    matriz = []
    # Quita los corchetes exteriores, ej: "[2,7,6],[9,5,1]"
    s_filas = input_str[1:-1]

    if not s_filas: # Maneja el caso de "[]"
        return matriz
    
    # Usa el truco del SEPARADOR
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        # Quita los corchetes de la fila, ej: "2,7,6"
        s_numeros = fila_str[1:-1]
        
        fila_numeros = []
        if s_numeros: # Revisa que la fila no esté vacía
            lista_de_strings_num = s_numeros.split(',') # ['2','7','6']
            for s_num in lista_de_strings_num:
                fila_numeros.append(int(s_num))
        
        # Solo añade si la fila tiene números
        if fila_numeros:
            matriz.append(fila_numeros)
    return matriz

# --- 1. PARSEO (Usando nuestra función) ---
matriz = parsear_matriz(input())

# --- 2. LÓGICA DEL CUADRADO MÁGICO ---

# Empezamos asumiendo que es verdad
es_magico = True
n = 0
suma_objetivo = 0

if not matriz or not matriz[0]: # Si la matriz está vacía
    es_magico = False
else:
    n = len(matriz) # Como es cuadrada, n = 3, 4, etc.
    
    # Paso 2a: Calcular la "suma mágica" objetivo
    # sum() es una función básica de Python, no una librería
    suma_objetivo = sum(matriz[0]) # Suma de la primera fila
    
    # Paso 2b: Comprobar el resto de las filas
    for i in range(1, n): # Empezamos en la fila 1
        if sum(matriz[i]) != suma_objetivo:
            es_magico = False
            break # Si una falla, paramos
    
    # Paso 2c: Comprobar las columnas (solo si las filas están bien)
    if es_magico:
        for j in range(n): # 'j' es el índice de la columna
            suma_columna = 0
            for i in range(n): # 'i' es el índice de la fila
                suma_columna += matriz[i][j]
            
            if suma_columna != suma_objetivo:
                es_magico = False
                break # Si una falla, paramos
                
    # Paso 2d: Comprobar las diagonales (solo si todo lo anterior está bien)
    if es_magico:
        suma_diag_principal = 0
        suma_diag_secundaria = 0
        for i in range(n):
            # Diagonal principal: [0][0], [1][1], [2][2]
            suma_diag_principal += matriz[i][i]
            # Diagonal secundaria: [0][2], [1][1], [2][0]
            suma_diag_secundaria += matriz[i][n - 1 - i]
            
        if suma_diag_principal != suma_objetivo or suma_diag_secundaria != suma_objetivo:
            es_magico = False

# --- 3. IMPRESIÓN ---
# Imprime el valor booleano (True o False)
print(es_magico)