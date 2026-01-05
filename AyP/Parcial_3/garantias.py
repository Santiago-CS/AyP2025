import pandas as pd
import numpy as np

def garantias_csv(path):
    rows = [
        "Agencia,Tramitadas,Monto,Cerradas,Facturado",
        "LM,40,381627,36,317515",
        "VR,35,167092,21,129840",
        "PV,15,96328,12,84312",
        ]
    with open(path, "w", encoding="utf-8") as f:
        for r in rows: f.write(r+"\n")

garantias_csv("garantias.csv")
df = pd.read_csv("garantias.csv")    #este se usa para importar el excel a python
print(df.head())                    #para corroborar imprime las primeras 5 filas del documento para ver que todo este bien
df.to_csv("garantias_out.csv", index=False) #este se usa para mandar de python a excel
#en caso que excel tenga otro formato
pd.read_
