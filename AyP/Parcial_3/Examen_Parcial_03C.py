import numpy as np
import pandas as pd

'''
Problema 01
Title: Estandarizar Lecturas de Sensores

Description:
Dado un array unidimensional con lecturas de un sensor, estandariza los
valores usando z-score:

    (x - mean(arr)) / std(arr)

Problem Statement:
Se recibe un array de enteros en formato literal, p.ej. [1,2,3,4].
Utiliza NumPy para convertirlo en un array y aplicar la fórmula anterior.
Retorna una lista de floats redondeados a dos decimales.
Si todos los elementos son iguales (desviación estándar 0), retorna una lista
de ceros.

Input Format:
  Una línea con un array literal.

Output Format:
  Lista de floats (redondeados a 2 decimales).
'''

def problem_01(arr):
    arr = np.array(arr, dtype=float)
    mean = np.mean(arr)
    stdev = np.std(arr)

    if stdev == 0:
        return [0.0] * len(arr)
    z_score = (arr - mean) / stdev

    return np.round(z_score, 2).tolist()
    #TU CÓDIGO AQUÍ (Recuerda quitar "pass")
    #pass

# Test Problem 01 (NO MODIFICAR)
_np_in = [
    [1,2,3],
    [5,5,5],
    [0,10,20],
    [-1,0,1],
    [100,200,300,400],
    [3,3,6,9],
    [7],
    [2,4,6,8,10],
    [10,0,10,0],
    [5,15,25]
]
_np_exp = [
    [-1.22, 0.0, 1.22],
    [0.0, 0.0, 0.0],
    [-1.22, 0.0, 1.22],
    [-1.22, 0.0, 1.22],
    [-1.34, -0.45, 0.45, 1.34],
    [-0.9, -0.9, 0.3, 1.51],
    [0.0],
    [-1.41, -0.71, 0.0, 0.71, 1.41],
    [1.0, -1.0, 1.0, -1.0],
    [-1.22, 0.0, 1.22]
]
correct = 0

for inp, exp in zip(_np_in, _np_exp):
    res = problem_01(inp)
    if np.all(res == exp):
        correct += 1
print(f"Problema 01 Parcial 03: {correct}/10")


'''
Problema 02
Title: Filtrar Clientes Frecuentes

Description:
Dado un diccionario con 'Client' y 'Purchases' (número de compras realizadas),
retorna el DataFrame con los clientes cuya Purchases >= 5.

Problem Statement:
Se recibe un dict con las claves:
  'Client': lista de strings
  'Purchases': lista de enteros
Utiliza pandas para crear un DataFrame y filtrar las filas donde
Purchases >= 5.
Retorna un DataFrame con los clientes en el orden original.

Input Format:
  Una línea con un dict literal.

Output Format:
  DataFrame filtrado.
'''

def problem_02(data):
    df = pd.DataFrame(data)
    filtrado = df[df["Purchases"]>= 5]

    return filtrado
    #TU CÓDIGO AQUÍ (Recuerda quitar "pass")
    #pass

# Test Problem 02 (NO MODIFICAR)
_pd_in = [
    {'Client':['A','B','C'],'Purchases':[4,5,6]},
    {'Client':['Tom'],'Purchases':[5]},
    {'Client':['Anna','Ben'],'Purchases':[1,2]},
    {'Client':['X','Y','Z'],'Purchases':[10,3,8]},
    {'Client':['P','Q','R','S'],'Purchases':[5,5,5,5]},
    {'Client':['A','B'],'Purchases':[0,100]},
    {'Client':['John','Doe','Smith'],'Purchases':[6,4,7]},
    {'Client':['M','N','O'],'Purchases':[1,2,3]},
    {'Client':['U','V','W'],'Purchases':[4,5,5]},
    {'Client':['K'],'Purchases':[0]}
]

_pd_exp = [
    {'Client':['B','C'],'Purchases':[5,6]},
    {'Client':['Tom'],'Purchases':[5]},
    {'Client':[],'Purchases':[]},
    {'Client':['X','Z'],'Purchases':[10,8]},
    {'Client':['P','Q','R','S'],'Purchases':[5,5,5,5]},
    {'Client':['B'],'Purchases':[100]},
    {'Client':['John','Smith'],'Purchases':[6,7]},
    {'Client':[],'Purchases':[]},
    {'Client':['V','W'],'Purchases':[5,5]},
    {'Client':[],'Purchases':[]}
]

correct = 0
for data, exp in zip(_pd_in, _pd_exp):
    res = None
    try:
        res = problem_02(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Client", "Purchases"])
    if isinstance(res, pd.DataFrame):
        res = res.reset_index(drop=True)
        try:
            exp_df = exp_df.astype(res.dtypes.to_dict())
        except TypeError:
            pass

        if res.equals(exp_df):
            correct += 1
print(f"Problema 02 Parcial 03: {correct}/10")


'''
Problema 03
Title: Filtrar Filas por Máximo

Description:
Dada una matriz, calcula el valor máximo de cada fila usando NumPy y luego
usa pandas para filtrar sólo las filas cuyo máximo sea mayor o igual a un
umbral dado.

Problem Statement:
Se recibe en dos líneas:
1) Una matriz 2D en formato literal (lista de listas de ints).
2) Un entero umbral.
Usa NumPy para calcular el máximo de cada fila y luego pandas para filtrar
las filas donde el máximo es mayor o igual al umbral.
Retorna la lista de filas filtradas (listas de ints), incluyendo el máximo
al final de cada fila.

Input Format:
  Línea 1: matriz literal.
  Línea 2: entero umbral.

Output Format:
  Lista de listas (filas filtradas con su máximo al final).
'''

def problem_03(mat, threshold):
    arr = np.array(mat)
    row_max = np.max(arr, axis=1)
    arr_with_max = np.column_stack((arr, row_max))#y aca traia un chilaquil asi todo chistoso jajsjsjsj

    df = pd.DataFrame(arr_with_max)

    filtrado = df[df.iloc[:, -1] >= threshold]

    return filtrado.values.tolist() #wow soy tonto solo por poner el guion bajo vio profe jajaja lmao
    #TU CÓDIGO AQUÍ (Recuerda quitar "pass")
    #pass


_comb_mat = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[0,0],[1,1],[2,2]],
    [[5]],
    [[1,2],[3,4],[5,6],[7,8]],
    [[10,20,30]],
    [[-1,-2,-3],[-4,-5,-6]],
    [[1,1,1],[2,2,2],[3,3,3]],
    [[5,5],[5,5],[5,5]],
    [[1,0,1],[0,1,0],[1,1,1]],
    [[100,200],[300,400]]
]
_comb_thr = [8,1,5,6,25,-2,2,5,1,350]
_comb_exp = [
    [[7, 8, 9, 9]],
    [[1, 1, 1], [2, 2, 2]],
    [[5, 5]],
    [[5, 6, 6], [7, 8, 8]],
    [[10, 20, 30, 30]],
    [[-1, -2, -3, -1]],
    [[2, 2, 2, 2], [3, 3, 3, 3]],
    [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
    [[1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1]],
    [[300, 400, 400]]
]

correct = 0
for mat, thr, exp in zip(_comb_mat, _comb_thr, _comb_exp):
    res = problem_03(mat, thr)
    if res == exp:
        correct += 1
print(f"Problema 03 Parcial 03: {correct}/10")
