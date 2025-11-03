# 1. Lee la entrada
input_str = input()

# 2. El Truco: Reemplaza y quita todos los corchetes
texto_limpio = input_str.replace('[', '').replace(']', '')

# 3. Revisa si el texto está vacío
if texto_limpio:
    # 4. Separa el texto por comas
    lista_de_strings = texto_limpio.split(',')
    
    # 5. Usa una comprensión de listas SIMPLE para convertir todo
    lista_plana = [int(s_num) for s_num in lista_de_strings]
else:
    # Caso para entradas como "[]" o "[[]]"
    lista_plana = []

# 6. Imprime el resultado
print(f"[{','.join(map(str, lista_plana))}]")