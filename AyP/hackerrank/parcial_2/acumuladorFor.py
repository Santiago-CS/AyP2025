# Leer el string desde la entrada
texto = input()

# Iniciar un contador para llevar la "suma" de los caracteres
contador = 0
    
# El ciclo 'for' recorre cada caracter en el texto, uno a la vez
for caracter in texto:
    # Por cada caracter encontrado, sumamos 1 al contador
    contador += 1

# Imprimir el resultado final
print(contador)