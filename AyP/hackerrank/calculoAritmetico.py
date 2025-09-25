s0 = float(input())
v0 = float(input())
a = float(input())
t = float(input())

s = s0 + v0 * t + 0.5 * a * t**2
v = v0 + a * t

print(f"{s:.3f} {v:.3f}")