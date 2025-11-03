x = input()
mayor = float("-inf")
menor = float("inf")

if x == "fin":
    print("No hay datos")
else:
    while x != "fin":
        x = float(x)
        maximo = max(x, mayor)
        minimo   = min(x, menor)
        mayor = maximo
        menor = minimo
        x = input()
        print("El dato mayor es: ", maximo, "y el numero minimo es: ", minimo)