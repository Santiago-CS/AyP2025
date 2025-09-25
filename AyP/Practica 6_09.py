h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())


h1 = h1 * 60
h2 = h2 * 60

if h1 > h2:
    tiempo = (24*60 - (h1 + m1)) + h2 + m2
else:
    tiempo = (h2 + m2) - (h1 + m1)

print(tiempo)
