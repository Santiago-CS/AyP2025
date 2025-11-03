# Lee la cadena de texto desde la entrada del usuario.
cadena = input()

# Inicia un contador para las vocales en cero.
contador_vocales = 0

# Define una cadena que contiene todas las vocales, tanto minúsculas como mayúsculas.
vocales = "aeiouAEIOU"

# Inicia un ciclo 'for' para recorrer cada carácter en la cadena de entrada.
for caracter in cadena:
    # Comprueba si el carácter actual se encuentra dentro de la cadena de vocales.
    if caracter in vocales:
        # Si es una vocal, incrementa el contador.
        contador_vocales += 1

# Imprime el número total de vocales encontradas.
print(contador_vocales)