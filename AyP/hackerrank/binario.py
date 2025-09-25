numero_decimal = int(input())

binario_con_etiqueta = bin(numero_decimal)

binario_sin_etiqueta = binario_con_etiqueta[2:]

binario_8_bits = binario_sin_etiqueta.zfill(8)

print(binario_8_bits)