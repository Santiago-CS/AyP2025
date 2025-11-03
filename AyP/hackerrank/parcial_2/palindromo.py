# Lee la palabra desde la entrada.
palabra = input()

# Obtenemos la longitud de la palabra para los cálculos de índices.
longitud = len(palabra)

# Iniciamos una "bandera" en True. Asumimos que es un palíndromo
# hasta que encontremos una prueba de que no lo es.
es_palindromo = True

# El ciclo 'for' solo necesita recorrer la PRIMERA MITAD de la palabra.
# Usamos '//' para la división entera, que funciona bien para longitudes pares e impares.
for i in range(longitud // 2):
    
    # Comparamos el carácter del inicio (i) con su correspondiente del final (longitud - 1 - i).
    if palabra[i] != palabra[longitud - 1 - i]:
        # Si encontramos un par que NO coincide, ya no es un palíndromo.
        # Cambiamos nuestra bandera a False.
        es_palindromo = False
        # Rompemos el ciclo porque no tiene caso seguir revisando.
        break

# Imprimimos el estado final de nuestra bandera.
print(es_palindromo)