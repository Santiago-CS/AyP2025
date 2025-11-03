# Leer la cantidad de palabras (N)
n = int(input())

# Iniciar un contador
contador = 0
resultado = ""

# El ciclo se ejecutará N veces
while contador < n:
    palabra = input()
    
    # Si la cadena de resultado no está vacía, añade un guion ANTES de la nueva palabra
    if resultado != "":
        resultado += "-"
    
    # Añade la palabra actual a la cadena
    resultado += palabra
    
    # Incrementa el contador
    contador += 1

print(resultado)