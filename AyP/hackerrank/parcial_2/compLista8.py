# 1. Lee la línea de entrada
input_str = input()

# 2. Quita los corchetes [ y ]
texto_sin_corchetes = input_str[1:-1]

elementos_pares_final = []

# 3. Revisa si la lista no está vacía
if texto_sin_corchetes:
    # 4. Divide el texto por las comas
    lista_cruda = texto_sin_corchetes.split(',')
    
    # 5. Obtiene la longitud
    n = len(lista_cruda)
    
    # 6. ¡COMPRENSIÓN DE LISTAS (Paso 1)!
    #    Obtiene los elementos en los índices pares (0, 2, 4...)
    #    Ej: ['1', '3', '5'] o ['"a"', '"c"']
    elementos_pares_crudos = [lista_cruda[i] for i in range(0, n, 2)]
    
    # 7. LIMPIEZA Y FORMATEO (Paso 2)
    #    Revisa el tipo del primer elemento
    if elementos_pares_crudos and elementos_pares_crudos[0].startswith('"'):
        # Comprensión para limpiar palabras (quitar comillas)
        elementos_pares_final = [item.strip('"') for item in elementos_pares_crudos]
    else:
        # Comprensión para limpiar números (convertir a int)
        elementos_pares_final = [int(item) for item in elementos_pares_crudos if item]

# 8. Imprime el resultado con el formato exacto (sin espacios)
#    repr() convierte una lista [1,3,5] a texto "[1, 3, 5]"
#    .replace(' ', '') le quita los espacios.
print(repr(elementos_pares_final).replace(' ', ''))