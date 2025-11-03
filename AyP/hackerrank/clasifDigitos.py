# Lee el número como una cadena de texto (string).
# No es necesario convertirlo a entero, ya que necesitamos recorrer sus dígitos.
numero_str = input()

# Inicia dos contadores en cero.
# Uno para los dígitos "bajos" (0-4) y otro para los "altos" (5-9).
contador_bajos = 0
contador_altos = 0

# Inicia un ciclo 'for' para recorrer cada carácter en el string del número.
for digito_caracter in numero_str:
    # Convierte el carácter actual a un número entero para poder compararlo.
    digito_valor = int(digito_caracter)
    
    # Comprueba si el valor del dígito es 4 o menos.
    if digito_valor <= 4:
        # Si es así, incrementa el contador de los dígitos bajos.
        contador_bajos += 1
    else:
        # Si no, significa que el dígito es 5 o mayor,
        # así que incrementa el contador de los dígitos altos.
        contador_altos += 1

# Imprime los dos contadores en una sola línea, separados por un espacio.
print(f"{contador_bajos} {contador_altos}")