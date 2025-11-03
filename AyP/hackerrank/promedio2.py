# Leer la cantidad de números (N)
n = int(input())

# Inicializar la suma y un contador manual
suma_total = 0.0
contador = 0

# El ciclo se ejecutará mientras el contador sea menor que n
while contador < n:
    # Leer cada número real (flotante) y sumarlo
    numero_real = float(input())
    suma_total += numero_real
    
    # Incrementar el contador para la siguiente vuelta
    contador += 1

# Calcular el promedio
promedio = suma_total / n

# Imprimir el resultado formateado con dos decimales
print(f"{promedio:.2f}")      