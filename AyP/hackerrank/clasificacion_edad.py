edad = int(input())

if edad <= 2:
    print("BEBE")
elif edad <= 12:
    print("NINO")
elif edad <= 17:
    print("ADOLESCENTE")
elif edad <= 64:
    print("ADULTO")
else:
    print("MAYOR")  