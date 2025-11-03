# Leer la cantidad de números (N)
n = int(input())

# Leer el PRIMER número y usarlo para inicializar min y max
primer_numero = int(input())
minimo = primer_numero
maximo = primer_numero

# Iniciar un contador en 1, porque ya leímos el primer número
contador = 1

# El ciclo se ejecuta para los N-1 números restantes
while contador < n:
    # Leer el siguiente número
    numero_actual = int(input())
    
    # Comprobar si es el nuevo máximo
    if numero_actual > maximo:
        maximo = numero_actual
        
    # Comprobar si es el nuevo mínimo
    if numero_actual < minimo:
        minimo = numero_actual
        
    # Incrementar el contador para la siguiente vuelta
    contador += 1

# Imprimir el resultado final
print(f"{minimo} {maximo}")