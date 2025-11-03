# Lee la cadena de texto desde la entrada.
cadena = input()

# Inicia dos contadores en cero, uno para cada tipo de letra.
contador_mayusculas = 0
contador_minusculas = 0

# Inicia un ciclo 'for' para recorrer cada carácter en la cadena.
for caracter in cadena:
    # Comprueba si el carácter es una letra mayúscula.
    if caracter.isupper():  
        contador_mayusculas += 1
    # Si no es mayúscula, comprueba si es una letra minúscula.
    elif caracter.islower():
        contador_minusculas += 1
    # Si no es ni mayúscula ni minúscula (es un espacio, número o símbolo),
    # no hacemos nada y el ciclo continúa con el siguiente carácter.

# Imprime los totales finales en una sola línea, separados por un espacio.
print(f"{contador_mayusculas} {contador_minusculas}")