# Leer la cantidad de datos (N)
n = int(input())

# Inicializar contadores para cada categoría
positivos = 0
negativos = 0
ceros = 0

# Inicializar un contador manual para el ciclo while
contador = 0

# El ciclo se repetirá mientras nuestro contador sea menor que n
while contador < n:
    # Leer el número de la línea actual
    numero = int(input())
    
    # Clasificar el número y aumentar el contador correspondiente
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1
        
    # Incrementar nuestro contador manualmente para avanzar a la siguiente repetición
    contador += 1

# Imprimir los resultados finales en una sola línea
print(positivos, negativos, ceros) 