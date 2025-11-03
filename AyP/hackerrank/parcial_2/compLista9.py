# 1. Lee la entrada
input_str = input()

# 2. Quita los corchetes [ y ]
texto_sin_corchetes = input_str[1:-1]

cuadrados_pares = []

# 3. Revisa si la entrada no fue "[]"
if texto_sin_corchetes:
    
    # 4. Separa el texto por las comas
    lista_de_strings = texto_sin_corchetes.split(',')

    # 5. ¡La Compresión de Listas!
    #    Se lee: "Crea una lista que contenga..."
    #    [int(s_num)**2        -> "...el cuadrado del número..."
    #     for s_num in ...    -> "...por cada 'texto de número' en la lista..."
    #     if int(s_num) % 2 == 0] -> "...SÓLO SI ese número es par."
    #
    #    Nota: convertimos a int() dos veces, una para el 'if' y otra para el cálculo
    cuadrados_pares = [int(s_num)**2 for s_num in lista_de_strings if int(s_num) % 2 == 0]

# 6. Imprime el resultado con el formato exacto
print(f"[{','.join(map(str, cuadrados_pares))}]")