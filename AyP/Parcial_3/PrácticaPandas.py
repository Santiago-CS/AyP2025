# Practica de pandas - 10 Problemas (Nivel Fácil)
# Cada sección contiene:
# 1) Descripción del problema (en comentarios)
# 2) Un espacio para que el alumno pegue su función de solución usando pandas
# 3) Un conjunto de test cases y un conteo de aciertos ("Problema X: correctos/10")

'''
Modifica únicamente el código dentro de cada función donde leas "Escribe aquí tu código", no modifiques ni elimines el resto
'''

import pandas as pd

# -----------------------------
# Problema 1: Suma de Columna "A"
# Title: Suma de Columna "A"
# Description:
# Dado un diccionario con la clave "A" que contiene números, conviértelo a DataFrame y calcula la suma de la columna "A".
# Input Format: Un dict con clave "A" -> lista de enteros.
# Output Format: Un entero: suma total de la columna.
# --------------------------------
def problem1(data):
    #Escribe aquí tu código
    # data: dict con clave "A"
    # Debe retornar la suma de la columna A
    df = pd.DataFrame(data)
    resultado = df['A'].sum()
    
    return resultado
    #pass

# TESTS Problema 1
_t1_in = [{"A":[1,2,3,4]},{"A":[10,20,30]},{"A":[5]},{"A":[0,0,0]},{"A":[1,1,1,1,1]},{"A":[2,4,6,8]},{"A":[100,200]},{"A":[7,3,5]},{"A":[10,0,10,0]},{"A":[9,9,9,9]}]
_t1_exp = [10,60,5,0,5,20,300,15,20,36]
correct = 0
for inp, exp in zip(_t1_in, _t1_exp):
    res = None
    try:
        res = problem1(inp)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 1: {correct}/10")

# -----------------------------
# Problema 2: Filtrar Estudiantes por Edad
# Title: Filtrar Estudiantes por Edad
# Description:
# Dado un dict con columnas "Name" y "Age" y un umbral, filtra filas donde Age > umbral.
# Input Format: Dict con "Name" y "Age", luego umbral (int).
# Output Format: DataFrame con columnas ["Name", "Age"] filtrado.
# --------------------------------
def problem2(data, threshold):
    #Escribe aquí tu código
    # data: dict con "Name" y "Age"
    # threshold: entero
    # Debe retornar DataFrame con filas donde Age > threshold
    df = pd.DataFrame(data)
    resultado = df[df['Age'] > threshold]

    return resultado
    #pass

# TESTS Problema 2
_t2_data = [
    {"Name":["Alice","Bob","Charlie"],"Age":[25,17,30]},
    {"Name":["John","Doe"],"Age":[18,22]},
    {"Name":["Anna"],"Age":[19]},
    {"Name":["Mike","Sara","Tom"],"Age":[16,20,21]},
    {"Name":["A","B","C"],"Age":[10,10,10]},
    {"Name":["X","Y","Z"],"Age":[30,25,20]},
    {"Name":["Alice","Bob"],"Age":[20,20]},
    {"Name":["Sam","Max","Leo"],"Age":[21,19,22]},
    {"Name":["Tom","Jerry"],"Age":[15,25]},
    {"Name":["A","B","C","D"],"Age":[18,19,20,21]}
]
_t2_thresh = [20,20,18,18,5,25,20,20,18,19]
_t2_exp = [
    [("Alice",25),("Charlie",30)],
    [("Doe",22)],
    [("Anna",19)],
    [("Sara",20),("Tom",21)],
    [("A",10),("B",10),("C",10)],
    [("X",30)],
    [],
    [("Sam",21),("Leo",22)],
    [("Jerry",25)],
    [("C",20),("D",21)]
]
correct = 0
for data, thr, exp in zip(_t2_data, _t2_thresh, _t2_exp):
    res = None
    try:
        res = problem2(data, thr)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Name", "Age"])
    if isinstance(res, pd.DataFrame):
        # Aseguramos mismo índice y mismos dtypes antes de comparar
        res = res.reset_index(drop=True)
        try:
            exp_df = exp_df.astype(res.dtypes.to_dict())
        except TypeError:
            # Por si alguna conversión falla, dejamos exp_df como está
            pass

        if res.equals(exp_df):
            correct += 1

print(f"Problema 2: {correct}/10")

# -----------------------------
# Problema 3: Agregar Columna Total
# Title: Agregar Columna Total
# Description:
# Dado un dict con listas "X" y "Y", crea DataFrame y añade columna "Total" = X + Y.
# Input Format: Dict con "X" y "Y".
# Output Format: DataFrame con columnas ["X","Y","Total"].
# --------------------------------
def problem3(data):
    #Escribe aquí tu código
    # data: dict con "X" y "Y"
    # Debe retornar DataFrame con columnas X, Y, Total
    df = pd.DataFrame(data)
    df['Total'] = df['X'] + df['Y']
    
    return df
    #pass

# TESTS Problema 3
_t3_data = [
    {"X":[1,2,3],"Y":[4,5,6]},
    {"X":[10],"Y":[20]},
    {"X":[0,0],"Y":[0,0]},
    {"X":[2,3],"Y":[3,4]},
    {"X":[1,1,1],"Y":[1,1,1]},
    {"X":[5,10],"Y":[5,10]},
    {"X":[7],"Y":[8]},
    {"X":[0,1,2],"Y":[3,4,5]},
    {"X":[1,2],"Y":[2,3]},
    {"X":[100,200,300],"Y":[400,500,600]}
]
_t3_exp = [
    [(1,4,5),(2,5,7),(3,6,9)],
    [(10,20,30)],
    [(0,0,0),(0,0,0)],
    [(2,3,5),(3,4,7)],
    [(1,1,2),(1,1,2),(1,1,2)],
    [(5,5,10),(10,10,20)],
    [(7,8,15)],
    [(0,3,3),(1,4,5),(2,5,7)],
    [(1,2,3),(2,3,5)],
    [(100,400,500),(200,500,700),(300,600,900)]
]
correct = 0
for data, exp in zip(_t3_data, _t3_exp):
    res = None
    try:
        res = problem3(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["X","Y","Total"])
    if isinstance(res, pd.DataFrame) and res.equals(exp_df):
        correct += 1
print(f"Problema 3: {correct}/10")

# -----------------------------
# Problema 4: Agrupar y Sumar por Categoría
# Title: Agrupar y Sumar
# Description:
# Dado dict con "Category" y "Value", agrupa por category y suma value de cada grupo.
# Input Format: Dict con "Category" y "Value".
# Output Format: DataFrame con columnas ["Category","Value"] (suma por categoría).
# --------------------------------
def problem4(data):
    #Escribe aquí tu código
    # data: dict con "Category" y "Value"
    # Debe retornar DataFrame con (Category, sum(Value))
    df = pd.DataFrame(data)
    resultado = df.groupby('Category', as_index=False)['Value'].sum() #grouby agrupa las filas segun la columna de su categoria 
    
    return resultado
    #pass

# TESTS Problema 4
_t4_data = [
    {"Category":["A","B","A","B"],"Value":[10,20,30,40]},
    {"Category":["X"],"Value":[100]},
    {"Category":["A","A","A"],"Value":[1,2,3]},
    {"Category":["D","E"],"Value":[50,50]},
    {"Category":["Cat","Dog","Cat"],"Value":[10,20,30]},
    {"Category":["A","B","C"],"Value":[5,5,5]},
    {"Category":["X","Y","X","Z"],"Value":[2,3,4,5]},
    {"Category":["P","P","Q","Q"],"Value":[10,20,30,40]},
    {"Category":["A","B","A"],"Value":[100,200,300]},
    {"Category":["M","N","M","N","M"],"Value":[1,2,3,4,5]}
]
_t4_exp = [
    [("A",40),("B",60)],
    [("X",100)],
    [("A",6)],
    [("D",50),("E",50)],
    [("Cat",40),("Dog",20)],
    [("A",5),("B",5),("C",5)],
    [("X",6),("Y",3),("Z",5)],
    [("P",30),("Q",70)],
    [("A",400),("B",200)],
    [("M",9),("N",6)]
]
correct = 0
for data, exp in zip(_t4_data, _t4_exp):
    res = None
    try:
        res = problem4(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Category","Value"])
    if isinstance(res, pd.DataFrame) and res.equals(exp_df):
        correct += 1
print(f"Problema 4: {correct}/10")

# -----------------------------
# Problema 5: Fila con Máximo Score
# Title: Fila con Máximo Score
# Description:
# Dado dict con "Name" y "Score", retorna la fila como Series con el Score máximo.
# Input Format: Dict con "Name" y "Score".
# Output Format: Series con índices "Name" y "Score".
# --------------------------------
def problem5(data):
    #Escribe aquí tu código
    # data: dict con "Name" y "Score"
    # Debe retornar una Series con la fila (Name, Score) de máximo Score
    df = pd.DataFrame(data)
    indice_del_maximo = df['Score'].idxmax() #.idmax consigue como la direccion de esa fila donde esta el dato maximo 
    resultado = df.loc[indice_del_maximo] #.loc para obtener toda la fila de ese índice
    
    return resultado
    pass

# TESTS Problema 5
_t5_data = [
    {"Name":["Alice","Bob","Charlie"],"Score":[85,92,88]},
    {"Name":["John"],"Score":[100]},
    {"Name":["A","B","C"],"Score":[70,70,60]},
    {"Name":["Tom","Jerry"],"Score":[50,75]},
    {"Name":["X","Y","Z"],"Score":[20,20,20]},
    {"Name":["Alpha","Beta"],"Score":[99,100]},
    {"Name":["One","Two","Three"],"Score":[10,5,15]},
    {"Name":["Kate","Leo"],"Score":[80,80]},
    {"Name":["M","N","O"],"Score":[30,40,35]},
    {"Name":["A","B","C"],"Score":[1,2,3]}
]
_t5_exp = [("Bob",92),("John",100),("A",70),("Jerry",75),("X",20),("Beta",100),("Three",15),("Kate",80),("N",40),("C",3)]
correct = 0
for data, exp in zip(_t5_data, _t5_exp):
    res = None
    try:
        res = problem5(data)
    except:
        pass
    name, score = exp
    exp_series = pd.Series({"Name": name, "Score": score})
    if isinstance(res, pd.Series) and res.equals(exp_series):
        correct += 1
print(f"Problema 5: {correct}/10")

# -----------------------------
# Problema 6: Ordenar por Precio
# Title: Ordenar por Precio
# Description:
# Dado dict con "Product" y "Price", retorna DataFrame ordenado por Price ascendente.
# Input Format: Dict con "Product" y "Price".
# Output Format: DataFrame con columnas ["Product","Price"] ordenado.
# --------------------------------
def problem6(data):
    #Escribe aquí tu código
    # data: dict con "Product" y "Price"
    # Debe retornar DataFrame ordenado por Price
    df = pd.DataFrame(data)
    precio_ordenado = df.sort_values(by='Price', ignore_index=True) #ignore_index le da orden a los indices de la izquierda de mi fila 

    return precio_ordenado
    #pass

# TESTS Problema 6
_t6_data = [
    {"Product":["apple","banana","cherry"],"Price":[3,1,2]},
    {"Product":["A"],"Price":[10]},
    {"Product":["X","Y"],"Price":[20,15]},
    {"Product":["p","q","r"],"Price":[5,5,6]},
    {"Product":["dog","cat"],"Price":[7,3]},
    {"Product":["A","B","C"],"Price":[100,50,75]},
    {"Product":["x","y"],"Price":[0,0]},
    {"Product":["m","n","o"],"Price":[2,3,1]},
    {"Product":["w","z","a"],"Price":[10,5,15]},
    {"Product":["book","pen"],"Price":[20,5]}
]
_t6_exp = [
    [("banana",1),("cherry",2),("apple",3)],
    [("A",10)],
    [("Y",15),("X",20)],
    [("p",5),("q",5),("r",6)],
    [("cat",3),("dog",7)],
    [("B",50),("C",75),("A",100)],
    [("x",0),("y",0)],
    [("o",1),("m",2),("n",3)],
    [("z",5),("w",10),("a",15)],
    [("pen",5),("book",20)]
]
correct = 0
for data, exp in zip(_t6_data, _t6_exp):
    res = None
    try:
        res = problem6(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Product","Price"])
    if isinstance(res, pd.DataFrame) and res.equals(exp_df):
        correct += 1
print(f"Problema 6: {correct}/10")

# -----------------------------
# Problema 7: Contar Colores
# Title: Contar Colores
# Description:
# Dado un dict con una columna "Color", retorna una Series de frecuencias de cada color.
# Input Format: Dict con clave "Color" -> lista de strings.
# Output Format: Series con índice = color, valor = conteo.
# --------------------------------
def problem7(data):
    #Escribe aquí tu código
    # data: dict con "Color"
    # Debe retornar un Series {color:count}
    df = pd.DataFrame(data)
    resultado = df['Color'].value_counts(sort=False)

    return resultado
    #pass

# TESTS Problema 7
_t7_in = [
    {"Color":["red","blue","red","green"]},
    {"Color":["yellow","yellow"]},
    {"Color":["black","white","black","white","black"]},
    {"Color":["red"]},
    {"Color":["a","b","a","c","a","b"]},
    {"Color":["blue","blue","blue"]},
    {"Color":["green","red","green","red","green","red"]},
    {"Color":["pink","purple"]},
    {"Color":["orange","orange","orange","orange"]},
    {"Color":["red","blue","green","blue"]}
]
_t7_exp = [
    {"red":2,"blue":1,"green":1},
    {"yellow":2},
    {"black":3,"white":2},
    {"red":1},
    {"a":3,"b":2,"c":1},
    {"blue":3},
    {"green":3,"red":3},
    {"pink":1,"purple":1},
    {"orange":4},
    {"red":1,"blue":2,"green":1}
]
correct = 0
for inp, exp in zip(_t7_in, _t7_exp):
    res = None
    try:
        res = problem7(inp)
    except:
        pass
    exp_series = pd.Series(exp)
    if isinstance(res, pd.Series) and res.equals(exp_series):
        correct += 1
print(f"Problema 7: {correct}/10")

# -----------------------------
# Problema 8: Filas Duplicadas
# Title: Filas Duplicadas
# Description:
# Dado un dict con "ID" y "Value", retorna DataFrame con filas donde ID se repite.
# Input Format: Dict con "ID" y "Value".
# Output Format: DataFrame con columnas ["ID","Value"] de filas duplicadas.
# --------------------------------
def problem8(data):
    #Escribe aquí tu código
    # data: dict con "ID" y "Value"
    # Debe retornar DataFrame de filas duplicadas (ID repetido)
 import pandas as pd

def problem8(data):
    #Escribe aquí tu código
    # data: dict con "ID" y "Value"
    # Debe retornar DataFrame de filas duplicadas (ID repetido)
    df = pd.DataFrame(data)
    duplicados = df[df.duplicated(subset='ID', keep=False)] #subset es en la columna que se fija y si son dos filas con el mismo ID pero diferente valor las detecta como diferentes
    #keep false marca como true los duplicados 
    return duplicados.reset_index(drop=True) #reset index borra los indices y pone de nuevo desde el o,1,2 etc 
#drop olvida el indice viejo para no crear columnas con los mismos 
    #pass

# TESTS Problema 8
_t8_data = [
    {"ID":[1,2,2,3,1],"Value":[10,20,30,40,50]},
    {"ID":[4,4,5,6],"Value":[100,200,300,400]},
    {"ID":[7,8,7],"Value":[5,6,7]},
    {"ID":[1,2,3,3],"Value":[10,20,30,40]},
    {"ID":[2,2,2],"Value":[1,2,3]},
    {"ID":[5,6,5,7],"Value":[10,20,30,40]},
    {"ID":[8,9,8,9],"Value":[100,200,300,400]},
    {"ID":[1,1,2],"Value":[5,10,15]},
    {"ID":[3,4,5,3],"Value":[20,30,40,50]},
    {"ID":[10,11,10,12,11],"Value":[1,2,3,4,5]}
]
_t8_exp = [
    [(1,10),(2,20),(2,30),(1,50)],
    [(4,100),(4,200)],
    [(7,5),(7,7)],
    [(3,30),(3,40)],
    [(2,1),(2,2),(2,3)],
    [(5,10),(5,30)],
    [(8,100),(9,200),(8,300),(9,400)],
    [(1,5),(1,10)],
    [(3,20),(3,50)],
    [(10,1),(11,2),(10,3),(11,5)]
]
correct = 0
for data, exp in zip(_t8_data, _t8_exp):
    res = None
    try:
        res = problem8(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["ID","Value"])
    if isinstance(res, pd.DataFrame) and res.equals(exp_df):
        correct += 1
print(f"Problema 8: {correct}/10")

# -----------------------------
# Problema 9: Pivotear Frecuencia por Categoría
# Title: Pivotear Frecuencia por Categoría
# Description:
# Dado dict con "Category" y "Value", crea pivot sumando Value por Category.
# Input Format: Dict con "Category" y "Value".
# Output Format: DataFrame con columnas ["Category","Value"] (suma por categoría).
# --------------------------------
def problem9(data):
    #Escribe aquí tu código
    # data: dict con "Category" y "Value"
    # Debe retornar DataFrame con (Category,sum(Value))
    df = pd.DataFrame(data)
    resultado = df.groupby('Category', as_index=False)['Value'].sum() #groupby hacia los montones , value elige la columna que sunmar y sum pues calcula el total
    
    return resultado
    #pass

# TESTS Problema 9
_t9_data = [
    {"Category":["A","B","A","B","C"],"Value":[10,20,30,40,50]},
    {"Category":["X"],"Value":[100]},
    {"Category":["A","A","A"],"Value":[1,2,3]},
    {"Category":["D","E"],"Value":[50,50]},
    {"Category":["cat","dog","cat"],"Value":[10,20,30]},
    {"Category":["A","B","C"],"Value":[5,5,5]},
    {"Category":["X","Y","X","Z"],"Value":[2,3,4,5]},
    {"Category":["P","P","Q","Q"],"Value":[10,20,30,40]},
    {"Category":["A","B","A"],"Value":[100,200,300]},
    {"Category":["M","N","M","N","M"],"Value":[1,2,3,4,5]}
]
_t9_exp = [
    [("A",40),("B",60),("C",50)],
    [("X",100)],
    [("A",6)],
    [("D",50),("E",50)],
    [("cat",40),("dog",20)],
    [("A",5),("B",5),("C",5)],
    [("X",6),("Y",3),("Z",5)],
    [("P",30),("Q",70)],
    [("A",400),("B",200)],
    [("M",9),("N",6)]
]
correct = 0
for data, exp in zip(_t9_data, _t9_exp):
    res = None
    try:
        res = problem9(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Category","Value"])
    if isinstance(res, pd.DataFrame) and res.equals(exp_df):
        correct += 1
print(f"Problema 9: {correct}/10")

# -----------------------------
# Problema 10: Promedio de Salarios
# Title: Promedio de Salarios
# Description:
# Dado un dict con "Salary", calcula la media y retorna float redondeado a dos decimales.
# Input Format: Dict con clave "Salary" -> lista de enteros.
# Output Format: Un float redondeado a 2 decimales.
# --------------------------------
def problem10(data):
    #Escribe aquí tu código
    # data: dict con "Salary"
    # Debe retornar promedio redondeado a 2 decimales
    df = pd.DataFrame(data)
    promedio = df['Salary'].mean()

    return round(promedio, 2)
    #pass

# TESTS Problema 10
_t10_data = [
    {"Salary":[1000,2000,3000,4000]},
    {"Salary":[500]},
    {"Salary":[100,200,300]},
    {"Salary":[0,0,0,0]},
    {"Salary":[1500,2500]},
    {"Salary":[1000,1000,1000,1000,1000]},
    {"Salary":[1200,1300,1100]},
    {"Salary":[2000,3000]},
    {"Salary":[4000,1000,3000]},
    {"Salary":[5000,4000,3000,2000,1000]}
]
_t10_exp = [2500.00,500.00,200.00,0.00,2000.00,1000.00,1200.00,2500.00,2666.67,3000.00]
correct = 0
for data, exp in zip(_t10_data, _t10_exp):
    res = None
    try:
        res = problem10(data)
    except:
        pass
    if isinstance(res, float) and abs(res - exp) < 0.01:
        correct += 1
print(f"Problema 10: {correct}/10")
