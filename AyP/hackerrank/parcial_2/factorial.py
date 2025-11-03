# Lee el número entero desde la entrada.
n = int(input())

# Inicializa la variable para guardar el resultado.
# Se inicia en 1 porque el factorial de 0 es 1 y porque
# multiplicar por 1 es el punto de partida para el cálculo.
factorial = 1

# Si n es mayor que 0, calculamos el producto.
if n > 0:
    # El ciclo 'for' recorre los números desde 1 hasta n (inclusive).
    for i in range(1, n + 1):
        # En cada paso, multiplica el resultado actual por el número del ciclo.
        factorial *= i

# Imprime el resultado final.
# Si n fue 0, el ciclo no se ejecuta y se imprime el valor inicial (1).
print(factorial)