# Lee el número desde la entrada. input() lo lee como una cadena de texto,
# lo cual es perfecto para este problema.
numero_como_cadena = input()

# Inicia una variable en cero para acumular la suma de los dígitos.
suma_total = 0

# Inicia un ciclo 'for' que recorre cada carácter de la cadena.
for digito_caracter in numero_como_cadena:
    # Convierte el carácter actual (que es texto, ej: "5") a su valor
    # numérico entero (ej: 5).
    valor_numerico = int(digito_caracter)
    
    # Añade ese valor a la suma total.
    suma_total += valor_numerico

# Imprime el resultado final de la suma.
print(suma_total)