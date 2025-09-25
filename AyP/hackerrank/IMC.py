peso = int(input())
altura = float(input())

imc = peso / (altura * altura)

if imc < 18.5:
    print("BAJO_PESO")
elif imc < 25:
    print("NORMAL")
elif imc < 30:
    print("SOBREPESO")
else:
    print("OBESIDAD") 