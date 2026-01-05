
# ===============================================================
# 19.- ARCHIVOS: MATPLOTLIB — BÁSICOS + INTEGRACIÓN CON NUMPY/PANDAS
# ===============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# B) FUNDAMENTOS PYLOT (plt) — (plt.show() comentado para scripts)
# ---------------------------------------------------------------
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.figure()
plt.plot(x, y, label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine")
plt.legend()
plt.show()

# Scatter
xs = np.array([1,2,3,4,5])
ys = np.array([2,1,3,5,4])
plt.figure()
plt.scatter(xs, ys, label="points")
plt.legend()
plt.title("Scatter demo")
plt.show()

# Barras
labels = ["A","B","C"]
vals = [10, 15, 7]
plt.figure()
plt.bar(labels, vals)
plt.title("Bar chart")
plt.show()

# Histograma
data = np.random.randn(200)
plt.figure()
plt.hist(data, bins=20)
plt.title("Histogram")
plt.show()

# Boxplot
plt.figure()
plt.boxplot([np.random.randn(100), np.random.randn(100)+1.5])
plt.title("Two-box comparison")
plt.show()

# Subplots
fig, ax = plt.subplots(1,2, figsize=(8,3))
ax[0].plot(x, y)
ax[0].set_title("Sin")
ax[1].plot(x, np.cos(x))
ax[1].set_title("Cos")
fig.suptitle("Trigonometry")
plt.show()

# ---------------------------------------------------------------
# C) INTEGRACIÓN CON NUMPY/PANDAS + DATASETS PRE-CARGADOS
# ---------------------------------------------------------------
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = np.array([12, 14, 15, 18, 22, 25, 23, 20, 19, 17, 16, 18], dtype=float)
df_sales = pd.DataFrame({"month": months, "sales": sales})

# Con NumPy (línea):
plt.figure()
plt.plot(np.arange(12), sales, marker="o")
plt.xticks(np.arange(12), months)
plt.title("Monthly Sales (NumPy)")
plt.show()

# Con pandas (barras):
ax = df_sales.plot(x="month", y="sales", kind="line", legend=False, title="Monthly Sales (pandas)", colormap="viridis")
plt.show()

# Guardar figura:
plt.figure()
plt.plot(sales)
plt.title("Savefig example")
plt.savefig("sales_plot.png")

# ---------------------------------------------------------------
# D) CASOS GUIADOS CON DATASETS
# ---------------------------------------------------------------
def create_people_dataset():
    rows = [
        "id,age,height,weight,city,gender",
        "1,21,1.65,60,CDMX,F",
        "2,19,1.72,72,Monterrey,M",
        "3,22,1.58,55,Guadalajara,F",
        "4,20,1.80,80,CDMX,M",
        "5,21,1.70,65,Guadalajara,F",
        "6,23,1.75,77,CDMX,M"
    ]
    with open("people_mpl.csv","w",encoding="utf-8") as f:
        for r in rows: f.write(r+"\n")

create_people_dataset()
df = pd.read_csv("people_mpl.csv")
# Dispersión altura vs. peso por género:
plt.figure()
m = df["gender"]=="M"
plt.scatter(df.loc[m,"height"], df.loc[m,"weight"], label="M")
plt.scatter(df.loc[~m,"height"], df.loc[~m,"weight"], label="F")
plt.xlabel("height")
plt.ylabel("weight")
plt.legend()
plt.title("Height vs Weight")
plt.show()

# Boxplot de peso por ciudad
plt.figure()
groups = [df[df["city"]=="CDMX"]["weight"], df[df["city"]=="Monterrey"]["weight"], df[df["city"]=="Guadalajara"]["weight"]]
plt.boxplot(groups, labels=["CDMX","Monterrey","Guadalajara"])
plt.title("Weight by City")
plt.show()

# ---------------------------------------------------------------
# E) BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# - Una figura por idea; títulos y etiquetas claras.
# - Leyendas legibles; grid/ticks cuando aporten.
# - Guardar con savefig para reportes reproducibles.