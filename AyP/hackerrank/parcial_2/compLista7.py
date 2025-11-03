import ast

# 1. Lee y convierte la entrada de texto a una lista real
lista_original = ast.literal_eval(input())

# 2. Obtiene la longitud de la lista
n = len(lista_original)

# 3. ¡La Comprensión de Listas!
#    Se lee: "Crea una lista que contenga..."
#    [lista_original[i] -> "...el elemento en la posición 'i'..."
#     for i in ...     -> "...por cada 'i' en el rango que empieza en 0,
#                          termina en n, y salta de 2 en 2."
elementos_pares = [lista_original[i] for i in range(0, n, 2)]

# 4. Imprime el resultado con el formato exacto (sin espacios)
print(repr(elementos_pares).replace(' ', ''))