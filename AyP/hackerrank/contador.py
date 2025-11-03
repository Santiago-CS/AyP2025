# Leer la cantidad de datos (N)
n = int(input())

# Inicializar la suma y un contador
suma_total = 0
contador = 0

# El ciclo se ejecutará mientras el contador sea menor que n
while contador < n:
    numero = int(input())
    suma_total += numero
    
    # ¡Importante! Incrementar el contador en cada vuelta
    contador += 1

print(suma_total)       