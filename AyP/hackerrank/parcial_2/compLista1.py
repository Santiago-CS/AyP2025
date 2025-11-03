# 1. Lee el entero n desde la entrada estándar.
n = int(input())

# 2. Crea una lista vacía para almacenar los resultados.
cuadrados = []

# 3. Usa un ciclo for para recorrer los números de 1 a n.
# range(1, n + 1) genera la secuencia: 1, 2, 3, ..., n.
for numero in range(1, n + 1):
    # Calcula el cuadrado del número actual.
    calculo = numero ** 2
    # Agrega el resultado a la lista.
    cuadrados.append(calculo) 

# 4. Imprime la lista final.
print(str(cuadrados).replace(",",","))