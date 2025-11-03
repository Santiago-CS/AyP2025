# 1. Lee la entrada como una cadena de texto.
input_str = input()

# 2. Quita los corchetes de los extremos usando "slicing".
# s[1:-1] toma desde el segundo carácter hasta el penúltimo.
numeros_str = input_str[1:-1]

# Lista para guardar los números pares que encontremos.
numeros_pares = []

# 3. Revisa si la cadena no está vacía antes de dividirla.
# Esto maneja el caso de una entrada como "[]".
if numeros_str:
    # 4. Divide la cadena por las comas para obtener una lista de strings.
    lista_de_strings = numeros_str.split(',')
    
    # 5. Itera sobre cada string en la lista.
    for s_num in lista_de_strings:
        # Convierte el string a un número entero.
        numero = int(s_num)
        
        # Comprueba si el número es par.
        if numero % 2 == 0:
            # Si es par, lo añade a nuestra lista de resultados.
            numeros_pares.append(numero)

# Imprime la lista final con el formato exacto (sin espacios).
print(f"[{','.join(map(str, numeros_pares))}]")