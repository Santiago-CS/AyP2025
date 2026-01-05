# 17.- ARCHIVOS: NUMPY — ARREGLOS, VECTORIZACIÓN, BROADCASTING, I/O

import numpy as np

# ---------------------------------------------------------------
# B) ARREGLOS: CREACIÓN, DTYPE, SHAPE
# ---------------------------------------------------------------
a = np.array([1, 2, 3], dtype=np.int64)
b = np.array([[1.0, 2.0], [3.0, 4.0]])
print("a:", a, "| dtype:", a.dtype, "| shape:", a.shape)
print("b:\n", b, "| dtype:", b.dtype, "| shape:", b.shape)
#para sumar 1 a los elementos de la lista por ejemplo se pone la variable a + 1 


x = [1, 2, 3]
y = []
for numeros in x:
    y.append(numeros + 1)
y
print (np.version)

zeros = np.zeros((2, 3))
ones  = np.ones((2, 3))
ar    = np.arange(0, 10, 2)           # [0,2,4,6,8] (Inicio, fin(sin incluir), paso)
lin   = np.linspace(0.0, 1.0, 5)      # 5 puntos entre 0 y 1
full7 = np.full((2,2), 7)             #para un numero especifico se usa este ya que la funcion ceros y unos es especifica
eye3  = np.eye(3, dtype=int)
print(zeros, ones, ar, lin, full7, eye3, sep="\n")

# ---------------------------------------------------------------
# C) INDEXACIÓN Y SLICING; VISTAS VS. COPIAS
# ---------------------------------------------------------------
v = np.arange(10)  # [0..9]
print(v[3])
print(v[2:7])
print( v[:5], v[5:])

M = np.arange(12).reshape(3,4)
print(M)
print(M[1,2])
print(M[0:2,1:3]) #fila del 0 al 1 (sin incluir al dos), columnas 1 y 2 no se incluye el 3

# Vistas comparten memoria:
s = v[2:7]
s[:] = -1
print(v)  # también cambia v

# Copia explícita:
v_copy = v.copy(); v_copy[0]=999
print(v_copy, v)

# 3D básico (didáctico):
T = np.arange(24).reshape(2,3,4)  # (profundidad, filas, cols)
print(T.shape, T[1,::2,2])

# ---------------------------------------------------------------
# D) VECTORIZACIÓN, UFUNCS Y BROADCASTING
# ---------------------------------------------------------------
x = np.array([1,2,3,4.])
y = np.array([10,20,30,40.])
print(x+y, x*y,  x**2, y**2)

# Broadcasting (3,1) + (3,) => (3,3)
col = np.array([[1],[2],[3]])
row = np.array([10,20,30])
print(col + row)

angles = np.linspace(0, np.pi, 5)
print(np.sin(angles))
print(np.exp([0,1,2]))

# ---------------------------------------------------------------
# E) AGREGACIONES Y ESTADÍSTICAS
# ---------------------------------------------------------------
A = np.arange(1,13).reshape(3,4)
print(A)
print(A.sum(), A.sum(axis=0), A.sum(axis=1))
print(A.mean(), A.std(), A.min(), A.max())
print(A.argmin(), A.argmax())

# ---------------------------------------------------------------
# F) MASKS, WHERE, UNIQUE, SET OPS
# ---------------------------------------------------------------
B = np.array([3,8,1,5,8,2,8])
mask = (B==8)
print(mask, B[mask])
print(np.where(B>3,1,0))
print(np.unique(B))
 
C = np.array([1,2,3,4,5])
D = np.array([4,5,6,7])
print(np.intersect1d(C,D))
print(np.union1d(C,D))
print(np.setdiff1d(C,D))

# ---------------------------------------------------------------
# G) RESHAPE, CONCAT, APILADO
# ---------------------------------------------------------------
X = np.arange(6).reshape(2,3)
Y = np.arange(6,12).reshape(2,3)
print(np.vstack([X,Y])) #agrupa arrays de forma vertical
print(np.hstack([X,Y]))
print(np.concatenate([X,Y], axis=0))    #vertical
print(np.concatenate([X,Y], axis=1))    #horizontal

# ---------------------------------------------------------------
# H) I/O CON NUMPY: loadtxt, genfromtxt, savetxt
    # ---------------------------------------------------------------
def create_num_csv(path):
    """Crea un CSV con columnas: id, x, y (y = 2.5*x + 3)."""
    ids = np.arange(1,11).reshape(-1,1)
    x = np.linspace(0.0, 9.0, 10).reshape(-1,1)
    y = x*2.5 + 3.0
    data = np.hstack([ids, x, y])
    np.savetxt(path, data, delimiter=",", fmt="%.6f")   #con esto guardas el excel

# Uso sugerido en clase:
create_num_csv("np_basic.csv")
data = np.loadtxt("np_basic.csv", delimiter=",")
print("loaded shape:", data.shape, "| head:\n", data[:5])
# =============================================================================
# I) ALEATORIOS (Generator, semilla, permutaciones, muestreos)
# =============================================================================

# --- Reproducibilidad básica (semilla fija) ---
rng = np.random.default_rng(42)
print(rng.integers(0, 10, size=5))

# --- Enteros aleatorios ---
# low inclusivo, high exclusivo
nums = rng.integers(low=10, high=20, size=8, endpoint=False)
print(nums)

# --- Permutaciones / Mezclas ---
arr = np.arange(10)
perm = rng.permutation(arr)     # NO modifica arr
rng.shuffle(arr)                # Mezcla IN-PLACE
print("Permutation:", perm, "| Shuffled:", arr)

# --- Muestreo con/ sin reemplazo ---
poblacion = np.array(list("ABCDEFGHIJ"))
muestra_sin = rng.choice(poblacion, size=5, replace=False)
muestra_con = rng.choice(poblacion, size=5, replace=True)
print("Sin reemplazo:", muestra_sin, "| Con reemplazo:", muestra_con)

# --- Muestreo ponderado (probabilidades p deben sumar 1) ---
p = np.array([0.20, 0.10, 0.05, 0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10])
muestra_p = rng.choice(poblacion, size=6, replace=True, p=p)
print("Muestreo ponderado:", muestra_p)

# --- Barajar filas de una matriz (mantener columnas alineadas) ---
X = rng.normal(0, 1, size=(5, 3))
idx = rng.permutation(X.shape[0])
X_barajado = X[idx]
print("Índices de barajado:", idx)

# =============================================================================
# J) NUMPY — DISTRIBUCIONES (parámetros, ejemplos y usos típicos)
# =============================================================================

# -------------------------------
# UNIFORME
# -------------------------------
a, b = 2.0, 5.0
x_uniforme = rng.uniform(a, b, size=1000)
print("Uniforme ~ U[2,5]: media≈", x_uniforme.mean(), " var≈", x_uniforme.var())

# -------------------------------
# NORMAL (Gaussiana)
# -------------------------------
mu, sigma = 10.0, 2.5
x_normal = rng.normal(loc=mu, scale=sigma, size=2000)
print("Normal N(10,2.5^2): media≈", x_normal.mean(), " var≈", x_normal.var())

# Estandarizada (media 0, var 1)
z = rng.standard_normal(2000)

# -------------------------------
# LOGNORMAL (si Y~N(mu, sigma^2) entonces X=exp(Y)~LogNormal)
# -------------------------------
mu_l, sigma_l = 0.0, 0.5
x_logn = rng.lognormal(mean=mu_l, sigma=sigma_l, size=2000)
print("LogNormal: media≈", x_logn.mean(), " mediana≈", np.median(x_logn))

# -------------------------------
# EXPONENCIAL (lambda = 1/scale)
# -------------------------------
scale = 3.0              # media = 3.0
x_exp = rng.exponential(scale=scale, size=3000)
print("Exponencial(scale=3): media≈", x_exp.mean())

# -------------------------------
# GAMMA (shape=k, scale=θ) — suma de k exponenciales (si k entero)
# -------------------------------
k, theta = 2.0, 2.0
x_gamma = rng.gamma(shape=k, scale=theta, size=3000)
print("Gamma(k=2,θ=2): media teórica=kθ=4 -> empírica≈", x_gamma.mean())

# -------------------------------
# BETA (en [0,1]) — útil para proporciones
# -------------------------------
a, b = 2.0, 5.0
x_beta = rng.beta(a, b, size=5000)
print("Beta(2,5): media teórica=a/(a+b)=0.2857 -> empírica≈", x_beta.mean())

# -------------------------------
# CHI-CUADRADO (k grados de libertad)
# -------------------------------
k = 5
x_chi2 = rng.chisquare(df=k, size=4000)
print("Chi^2(df=5): media teórica=df=5 -> empírica≈", x_chi2.mean())

# -------------------------------
# t DE STUDENT (df grados de libertad)
# -------------------------------
df = 10
x_t = rng.standard_t(df=df, size=4000)
print("t-Student(df=10): media≈", x_t.mean())

# -------------------------------
# BINOMIAL (n ensayos, p éxito) — # éxitos
# -------------------------------
n, p = 20, 0.3
x_bin = rng.binomial(n=n, p=p, size=5000)
print("Binomial(n=20,p=0.3): media teórica=np=6 -> empírica≈", x_bin.mean())

# -------------------------------
# POISSON (lambda) — recuento de eventos por intervalo
# -------------------------------
lam = 4.0
x_poi = rng.poisson(lam=lam, size=5000)
print("Poisson(λ=4): media teórica=4 -> empírica≈", x_poi.mean())

# -------------------------------
# GEOMÉTRICA (p) — # ensayos hasta 1er éxito (soporte 1,2,3,...)
# -------------------------------
p = 0.2
x_geo = rng.geometric(p=p, size=5000)
print("Geométrica(p=0.2): media teórica=1/p=5 -> empírica≈", x_geo.mean())

# -------------------------------
# MULTINOMIAL (n, p) — vector de recuentos en k categorías
# -------------------------------
p = np.array([0.5, 0.3, 0.2])
x_multi = rng.multinomial(n=20, pvals=p, size=3)  # 3 repeticiones
print("Multinomial (3 corridas, suman 20 c/u):\n", x_multi, "\nSuma filas:", x_multi.sum(axis=1))

# -------------------------------
# PROB-UTILIDADES: UÁR y elección ponderada
# -------------------------------
# Escenario: asignar aleatoriamente “expertos” a tickets con pesos por prioridad
tickets = np.arange(8)
expertos = np.array(["Ana", "Luis", "Maya"])
pesos = np.array([0.6, 0.3, 0.1])  # Ana más probable

asignado = []
for _ in tickets:
    asignado.append(rng.choice(expertos, p=pesos))
asignado = np.array(asignado)
print("Asignación ponderada:", asignado)

# ---------------------------------------------------------------
# K) CASOS GUIADOS
# ---------------------------------------------------------------
def minmax_scale(v):
    """Devuelve (v - min)/(max - min). Maneja caso max==min."""
    v = v.astype(float); mn=v.min(); mx=v.max()
    return np.zeros_like(v) if mx==mn else (v-mn)/(mx-mn)

def zscore_cols(M):
    """Estandariza columnas: (x - mu)/sigma, evitando división por cero."""
    M = M.astype(float); mu = M.mean(axis=0); sd = M.std(axis=0)
    sd = np.where(sd==0, 1.0, sd)
    return (M - mu) / sd

def pairwise_dist_2d(P):
    """Matriz de distancias euclidianas entre puntos 2D."""
    A = P[:,None,:]; B = P[None,:,:]
    return np.sqrt(((A-B)**2).sum(axis=2))

print(minmax_scale(np.array([5,10,15,20])))
print(zscore_cols(np.arange(12).reshape(3,4)))
print(pairwise_dist_2d(np.array([[0,0],[1,0],[1,1]])))

# ---------------------------------------------------------------
# J) VENTAJAS / DESVENTAJAS / BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas: velocidad, vectorización, broadcasting, API numérica rica.
# Desventajas: arreglos homogéneos, faltantes menos cómodos que en pandas.
# Buenas prácticas: documentar shapes; evitar copias innecesarias; preferir ufuncs.



def suma (a, b=2)
        return a + b
print(suma(3))

sdsdfsdf