# 1. Lee la línea de entrada como un texto
input_str = input()

# 2. Quita los corchetes [ y ] de los extremos.
#    input_str[1:-1] significa "dame el texto desde el segundo carácter hasta el penúltimo".
texto_sin_corchetes = input_str[1:-1]

# 3. Divide el texto por las comas.
#    El resultado es una lista de textos que TODAVÍA tienen comillas.
#    Ejemplo: ['"apple"', '"banana"']
lista_con_comillas = texto_sin_corchetes.split(',')

# 4. Crea una lista vacía para guardar los resultados limpios
lista_mayusculas = []

# 5. Inicia un ciclo para "limpiar" cada elemento
for palabra_sucia in lista_con_comillas:
    # 6. Quita las comillas (") de los extremos de cada palabra
    palabra_limpia = palabra_sucia.strip('"')
    
    # 7. Convierte la palabra limpia a mayúsculas
    palabra_final = palabra_limpia.upper()
    
    # 8. Agrega el resultado final a nuestra lista
    lista_mayusculas.append(palabra_final)

# 9. Imprime el resultado con el formato exacto que pide el ejemplo
#    (con comillas simples y sin espacios)
palabras_formateadas = [f"'{palabra}'" for palabra in lista_mayusculas]
print(f"[{','.join(palabras_formateadas)}]")