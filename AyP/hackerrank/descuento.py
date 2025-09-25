# Lee el total como un número real (flotante)
total = float(input())

# Aplica el descuento correspondiente
if total < 100:
    # 0% de descuento
    total_final = total
elif total < 500:
    # 5% de descuento
    total_final = total * 0.95
elif total < 1000:
    # 10% de descuento
    total_final = total * 0.90
else:
    # 15% de descuento
    total_final = total * 0.85

# Imprime el resultado final formateado a dos decimales
print(f"{total_final:.2f}")