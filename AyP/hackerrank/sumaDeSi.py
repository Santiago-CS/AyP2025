# Lee el número entero de 4 cifras.
n = int(input())

# 1. Obtiene el primer dígito (millares)
# La división entera entre 1000 elimina los últimos tres dígitos.
d1 = n // 1000

# 2. Obtiene el segundo dígito (centenas)
# Al dividir entre 100 se eliminan los dos últimos dígitos.
# El módulo 10 nos da el último dígito del resultado (que es la centena original).
d2 = (n // 100) % 10

# 3. Obtiene el tercer dígito (decenas)
# Al dividir entre 10 se elimina el último dígito.
# El módulo 10 nos da el nuevo último dígito (la decena original).
d3 = (n // 10) % 10

# 4. Obtiene el cuarto dígito (unidades)
# El módulo 10 siempre da el último dígito de un número.
d4 = n % 10

# Suma los cuatro dígitos que hemos aislado.
suma_de_digitos = d1 + d2 + d3 + d4

# Imprime el resultado final.
print(suma_de_digitos)