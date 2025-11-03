# --- 1. PARSEO (Leer la matriz sin librerías) ---
matriz = []
input_str = input() # Ej: "[[1,2],[2,1]]"

s_filas = input_str[1:-1] # Ej: "[1,2],[2,1]"

if s_filas:
    # Reemplazamos "],[" por un separador único
    s_filas_separadas = s_filas.replace('],[', ']SEPARADOR[')
    lista_filas_str = s_filas_separadas.split('SEPARADOR')

    for fila_str in lista_filas_str:
        s_numeros = fila_str[1:-1] # "1,2"
        
        fila_numeros = []
        if s_numeros:
            lista_de_strings_num = s_numeros.split(',') # ['1','2']
            for s_num in lista_de_strings_num:
                fila_numeros.append(int(s_num))
        
        if fila_numeros: # Previene error con "[[]]"
             matriz.append(fila_numeros)

# ¡Listo! 'matriz' ahora es [[1, 2], [2, 1]]

# --- 2. LÓGICA DE SIMETRÍA ---

# Asumimos que es verdad hasta que se demuestre lo contrario
es_simetrica = True
n = 0

if matriz:
    n = len(matriz) # Como es cuadrada, n = num de filas

# Recorremos las filas (i)
for i in range(n):
    
    # Recorremos las columnas (j), pero empezamos
    # DESPUÉS de la diagonal (j = i + 1)
    for j in range(i + 1, n):
        
        # ¡LA LÓGICA CLAVE!
        # Comparamos el elemento [i][j] con su "reflejo" [j][i]
        if matriz[i][j] != matriz[j][i]:
            
            # Si UNO falla, ya no es simétrica
            es_simetrica = False
            break # Salimos del ciclo 'j' (ya no hay que revisar esta fila)
    
    # Si el 'flag' ya es falso, salimos también del ciclo 'i'
    if not es_simetrica:
        break

# --- 3. IMPRESIÓN ---
if es_simetrica:
    print("YES")
else:
    print("NO")