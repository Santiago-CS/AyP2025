precio = int(input())
iva = int(input())

precio_final = precio * (1 + iva / 100)

print(f"{precio_final:.2f}")