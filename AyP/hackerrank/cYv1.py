C = float(input())
r = float(input())
m = float(input())
t = float(input())

M = C * (1 + (r / 100) / m) ** (m * t)
print(f"{M:.2f}")

