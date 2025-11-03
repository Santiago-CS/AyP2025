# Lee la cadena de entrada
s = input()

# Inicializa el contador de dígitos y el índice para el ciclo
contador_digitos = 0
i = 0

# Recorre la cadena usando un ciclo while
while i < len(s):
  # Obtiene el caracter en la posición actual
  caracter = s[i]
  
  # Verifica si el caracter es un dígito
  if caracter.isdigit():
    contador_digitos += 1
  
  # Incrementa el índice para pasar al siguiente caracter
  i += 1

# Imprime el resultado final
print(contador_digitos)