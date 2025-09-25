# 1. Pedimos la cadena al usuario
cadena_s = input()

# 2. ¡EL GUARDIA! Revisamos si la longitud es exactamente 12.
# Nota el doble signo de igual (==), que significa "¿es exactamente igual a?"
if len(cadena_s) == 12:

    seccion1 = cadena_s[0:3]
    seccion2 = cadena_s[3:6]
    seccion3 = cadena_s[6:9]
    seccion4 = cadena_s[9:12]

    # Unimos y mostramos el resultado final
    resultado_final = f"{seccion1}-{seccion2}-{seccion3}-{seccion4}"
    print(resultado_final)

else:
    
    print("Error: La cadena que escribiste NO tiene 12 caracteres.")
    print(f"Tú escribiste {len(cadena_s)} caracteres.")