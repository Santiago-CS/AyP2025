# Lee la cadena de texto original desde la entrada.
cadena_original = input()

# Inicia una cadena vacía donde construiremos la versión invertida.
cadena_invertida = ""

# Inicia un ciclo 'for' que recorre cada carácter de la cadena original.
for caracter in cadena_original:
    # En cada paso, coloca el carácter actual AL INICIO de la cadena invertida.
    cadena_invertida = caracter + cadena_invertida

# Imprime la cadena completamente invertida.
print(cadena_invertida)