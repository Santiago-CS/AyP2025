# 1. Lee la línea de entrada (ej: '["racecar","hello","madam"]')
# 1. Lee la línea de entrada
input_str = input()

# 2. Quita los corchetes [ y ]
texto_sin_corchetes = input_str[1:-1]

# 3. Divide el texto por las comas
lista_con_comillas = texto_sin_corchetes.split(',')

# 4. ¡La Comprensión de Listas con Filtro!
#    Se lee: "Crea una lista que contenga..."
#    [p.strip('"')         -> "...la palabra limpia (sin comillas)..."
#     for p in ...         -> "...por cada palabra 'sucia' en la lista..."
#     if p.strip('"') == p.strip('"')[::-1]] -> "...SÓLO SI la palabra limpia es igual a su reverso."
#
#    (Sí, p.strip('"') se repite, pero es la forma de hacerlo en una sola comprensión)
lista_palindromos = [p.strip('"') for p in lista_con_comillas if p.strip('"') == p.strip('"')[::-1]]

# 5. Imprime el resultado con el formato exacto
palabras_formateadas = [f"'{p}'" for p in lista_palindromos]
print(f"[{','.join(palabras_formateadas)}]")