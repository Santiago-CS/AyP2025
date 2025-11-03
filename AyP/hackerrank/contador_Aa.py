# Inicializa el contador total de letras 'a' y 'A'.
contador_a = 0

# Lee la primera línea de texto.
linea = input()

# Bucle principal: se ejecuta mientras la línea no sea "FIN".
while linea != "FIN":
  # Inicializa el índice para recorrer los caracteres de la línea actual.
  i = 0
  
  # Bucle anidado: recorre cada caracter de la línea actual.
  while i < len(linea):
    caracter = linea[i]
    # Comprueba si el caracter es 'a' o 'A'.
    if caracter == 'a' or caracter == 'A':
      contador_a += 1
    # Avanza al siguiente caracter.
    i += 1
  
  # Lee la siguiente línea para la próxima iteración del bucle principal.
  linea = input()

# Imprime el resultado final.
print(contador_a)