kwh = float(input())

costo = 0

costo += min(kwh, 100) * 0.50

costo += max(min(kwh, 200) - 100, 0) * 0.75

costo += max(kwh - 200, 0) * 1.20

print(f"{costo:.2f}")
