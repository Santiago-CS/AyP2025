#Asignacion simple (variable -> valor)

curso = "Algoritmos y Programación" #str(Cadenas de texto o palabras)

creditos = 8 #int(enteros)
calificacion_promedio= 9.1 #float (decimales)

flag = True #bool (true or false)



Nombre  = input("Ingresa tu nombre:\n")

edad = int(input("Ingresa tu edad:\n"))

#para imprimir (Salida de datos) se puede de dos maneras la clasica:
print("Tu nombre es", Nombre, "y tienes", edad, "años")

#esta donde ponemos una f al inicio de las comillas y ponemos las variables entre parentesis
print(f"Tu nombre es{Nombre} y tienes {edad} años")


#Primer ejercicio de practica

a = int(input())
b = int (input())

suma = a + b

print(suma)


base = float(input())
altura = float(input())

area = base*altura
perimetro = base + base + altura + altura

print(area,perimetro)