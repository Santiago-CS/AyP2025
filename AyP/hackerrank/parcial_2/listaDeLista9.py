def parsear_matriz(input_str):
    """
    Función auxiliar para convertir un string "[[1,0],[0,1]]"
    en una lista de listas [[1, 0], [0, 1]] sin usar librerías.
    """
    matriz = []
    s_filas = input_str[1:-1] # Quita corchetes exteriores
    if not s_filas: return []
    
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        s_numeros = fila_str[1:-1] # Quita corchetes de la fila
        
        if s_numeros:
            # Usamos una comprensión para acortar la conversión
            matriz.append([int(s_num) for s_num in s_numeros.split(',')])
        elif fila_str == "[]": # Maneja caso de "[[]]"
            matriz.append([])
            
    return matriz

# --- 1. PARSEO ---
matriz = parsear_matriz(input())

# --- 2. LÓGICA (Contar y Hundir) ---

# Revisa si la matriz está vacía
if not matriz or not matriz[0]:
    print(0)
else:
    contador_islas = 0
    num_filas = len(matriz)
    num_cols = len(matriz[0])
    
    # Recorre cada celda de la matriz
    for i in range(num_filas):
        for j in range(num_cols):
            
            # ¡LA CLAVE! Si encontramos tierra...
            if matriz[i][j] == 1:
                
                # 1. La contamos como una nueva isla
                contador_islas += 1
                
                # 2. La "hundimos" (iniciamos el DFS)
                
                # 'stack' es nuestra "lista de tareas pendientes"
                # Empezamos con la celda que acabamos de encontrar
                stack = [(i, j)]
                
                # Hundimos esta primera celda para no volver a
                # procesarla
                matriz[i][j] = 0 
                
                # Mientras haya tareas pendientes...
                while stack:
                    # Saca la última tarea
                    (fila, col) = stack.pop()
                    
                    # Define los 4 posibles vecinos (arriba, abajo, izq, der)
                    vecinos = [
                        (fila + 1, col), # Abajo
                        (fila - 1, col), # Arriba
                        (fila, col + 1), # Derecha
                        (fila, col - 1)  # Izquierda
                    ]
                    
                    for (v_fila, v_col) in vecinos:
                        # Comprueba que el vecino esté DENTRO del mapa
                        if 0 <= v_fila < num_filas and 0 <= v_col < num_cols:
                            
                            # Comprueba si ese vecino es TIERRA (1)
                            if matriz[v_fila][v_col] == 1:
                                
                                # ¡Lo encontramos! Lo hundimos...
                                matriz[v_fila][v_col] = 0
                                # ...y lo añadimos a la lista de tareas
                                # para explorar SUS vecinos después
                                stack.append((v_fila, v_col))

    # --- 3. IMPRESIÓN ---
    print(contador_islas)