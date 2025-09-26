# Lee las longitudes de los tres lados como números flotantes
a = float(input())
b = float(input())
c = float(input())

# Comprueba la igualdad de los lados en orden de especificidad
if a == b and b == c:
    print("EQUILATERO")
elif a == b or b == c or a == c:
    print("ISOCELES")
else:
    print("ESCALENO")