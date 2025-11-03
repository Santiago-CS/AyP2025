# Lee el número en formato de string.
numero_str = input()

# Inicializa una variable para guardar el dígito más alto encontrado hasta el momento.
# Empezamos con -1, ya que cualquier dígito (0-9) será mayor.
digito_maximo = -1

# Inicia un ciclo para recorrer cada carácter (dígito) en el string.
for caracter_digito in numero_str:
    # Convierte el carácter a su valor numérico entero.
    valor_digito = int(caracter_digito)
    
    # Compara el dígito actual con el máximo que hemos encontrado hasta ahora.
    if valor_digito > digito_maximo:
        # Si el actual es más grande, lo guardamos como el nuevo máximo.
        digito_maximo = valor_digito

# Imprime el valor máximo encontrado después de revisar todos los dígitos.
print(digito_maximo)