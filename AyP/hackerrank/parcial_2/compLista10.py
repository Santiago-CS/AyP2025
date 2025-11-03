# 1. Lee la entrada (ej: "[1,2,3,4,5]")
input_str = input()

# 2. Quita los corchetes [ y ]
texto_sin_corchetes = input_str[1:-1]

lista_numeros = []
# 3. Revisa si la entrada no está vacía
if texto_sin_corchetes.strip():
    # 4. Separa por comas y convierte a números
    lista_numeros = [int(s_num) for s_num in texto_sin_corchetes.split(',')]

# 5. ¡LA LÓGICA CLAVE!
#    Inicializa la suma ACUMULATIVA fuera de la lista
suma_total = 0

# 6. ¡La Compresión de Listas!
#    Se lee: "Crea una lista que contenga..."
#    [suma_total := ... -> "...el valor de 'suma_total' DESPUÉS de asignarle..."
#     ... := suma_total + num -> "...el valor de 'suma_total' anterior + el 'num' actual..."
#     for num in ...]    -> "...por cada 'num' en la lista de números."
#
lista_acumulativa = [suma_total := suma_total + num for num in lista_numeros]

# 7. Imprime el resultado con el formato exacto
print(f"[{','.join(map(str, lista_acumulativa))}]")