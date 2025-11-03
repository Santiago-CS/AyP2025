enteros = input()
lista_enteros = enteros[1:-1]
numeros_en_texto = lista_enteros.split(",")

lista = []
for n in numeros_en_texto:
    if n:
        lista.append(int(n))


suma_par = 0
i = 0

while i < len(lista):
    numeroActual = lista[i]
    
    if numeroActual % 2 == 0:
        suma_par += numeroActual
    
    i += 1

print(suma_par)