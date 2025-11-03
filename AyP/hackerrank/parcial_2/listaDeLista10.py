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
            # Usamos una comprensión para acortar la conversión
            fila_numeros = [int(s_num) for s_num in lista_de_strings_num]
        
        if fila_numeros: # Solo añade si la fila tiene números
            matriz.append(fila_numeros)
            
    return matriz

# --- 1. PARSEO ---
matriz = parsear_matriz(input())

# --- 2. LÓGICA (Probar todos los rectángulos) ---

if not matriz or not matriz[0]:
    print(0) # O un valor de error, aunque las constraints dicen que no está vacía
else:
    num_filas = len(matriz)
    num_cols = len(matriz[0])
    
    # Inicializamos la suma máxima con el primer elemento.
    # Esto es importante para que funcione con matrices de puros
    # números negativos (como el Sample 1).
    max_suma_global = matriz[0][0]
    
    # Ciclo 1: Define la FILA de INICIO (r1)
    for r1 in range(num_filas):
        
        # Ciclo 2: Define la COLUMNA de INICIO (c1)
        for c1 in range(num_cols):
            
            # Ciclo 3: Define la FILA de FIN (r2)
            # (Empieza desde r1)
            for r2 in range(r1, num_filas):
                
                # Ciclo 4: Define la COLUMNA de FIN (c2)
                # (Empieza desde c1)
                for c2 in range(c1, num_cols):
                    
                    # --- Ahora tenemos un rectángulo definido ---
                    # (desde [r1][c1] hasta [r2][c2])
                    
                    suma_actual_rectangulo = 0
                    
                    # Ciclo 5: Suma las filas (i) de este rectángulo
                    for i in range(r1, r2 + 1):
                        
                        # Ciclo 6: Suma las columnas (j) de este rectángulo
                        for j in range(c1, c2 + 1):
                            suma_actual_rectangulo += matriz[i][j]
                            
                    # Comparamos la suma de este rectángulo con
                    # la máxima que llevamos guardada
                    if suma_actual_rectangulo > max_suma_global:
                        max_suma_global = suma_actual_rectangulo

    # --- 3. IMPRESIÓN ---
    print(max_suma_global)