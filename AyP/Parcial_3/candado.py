def candado_examen(c1,c2,c3, c4, c5, c6, c7):
    suma = c1 + c2 + c3 + c4 + c5 + c6 + c7 
    promedio = suma / 7
    if c1 + c2 + c3 + c4 + c5 + c6 + c7 < 420:
        return "No pasa el candado", suma , promedio
    else:
        return "Si pasa el candado", suma , promedio

candado_examen(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))