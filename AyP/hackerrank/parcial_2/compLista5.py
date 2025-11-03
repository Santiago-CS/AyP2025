# 1. Lee el número n
n = int(input())

# 2. ¡La Comprensión de Listas con Filtro!
#    Se lee: "Crea una lista que contenga..."
#    [i               -> "...el número 'i'..."
#     for i in ...   -> "...por cada 'i' en el rango de 1 a n..."
#     if n % i == 0] -> "...SÓLO SI el residuo de n / i es 0."
divisores = [i for i in range(1, n + 1) if n % i == 0]

# 3. Imprime la lista con el formato exacto (sin espacios)
#    (Como en los ejercicios anteriores, esto es para evitar errores
#    de formato por los espacios que Python pone por defecto).
print(f"[{','.join(map(str, divisores))}]")