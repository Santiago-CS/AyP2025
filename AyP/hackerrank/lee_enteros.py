# Inicializa la variable para guardar la suma total.
suma_total = 0

# Lee el primer número para iniciar el ciclo.
numero = int(input())

# El ciclo se ejecuta mientras el número leído no sea 0.
while numero != 0:
  # Agrega el número actual a la suma total.
  suma_total += numero
  # Lee el siguiente número.
  numero = int(input())

# Imprime el resultado final.
print(suma_total)