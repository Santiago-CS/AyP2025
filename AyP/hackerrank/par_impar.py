n = int(input())

if n == 0:
    print("CERO")
elif n > 0 and n % 2 == 0:
    print("POSITIVO_PAR")
elif n > 0 and n % 2 != 0:
    print("POSITIVO_IMPAR")
elif n < 0 and n % 2 == 0:
    print("NEGATIVO_PAR")
elif n < 0 and n % 2 != 0:
    print("NEGATIVO_IMPAR")