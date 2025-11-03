# Lee el tamaño de la figura desde la entrada.
n = int(input())

# El primer ciclo 'for' recorre cada fila, de 0 a n-1.
# La variable 'i' representa el número de la fila actual.
for i in range(n):
    
    # Inicia una cadena vacía para construir la línea actual.
    linea_actual = ""
    
    # El segundo ciclo 'for' recorre cada columna de la fila actual, de 0 a n-1.
    # La variable 'j' representa el número de la columna actual.
    for j in range(n):
        
        # Esta es la condición clave para dibujar la 'X'.
        # Comprueba si la columna 'j' está en la diagonal principal (j == i)
        # O si está en la diagonal secundaria (j == n - 1 - i).
        if j == i or j == n - 1 - i:
            # Si se cumple, añade una 'X' a la línea.
            linea_actual += "X"
        else:
            # Si no, añade un espacio.
            linea_actual += " "
            
    # Después de construir toda la línea, la imprime.
    print(linea_actual)