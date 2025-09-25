hora = int(input())
minuto = int(input())

hora_12 = 0
periodo = ""

if hora == 0:
    hora_12 = 12
    periodo = "AM"
elif hora < 12:
    hora_12 = hora
    periodo = "AM"
elif hora == 12:
    hora_12 = 12
    periodo = "PM"
    
else:  
    hora_12 = hora - 12
    periodo = "PM"

print(f"{hora_12:02d}:{minuto:02d} {periodo}")