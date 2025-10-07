import numpy as np
# numpy usa ndarray che sono array ottimizzati che possono avere solo un tipo di dato 
a: list[int] = [1, 2, 3] 
a_vec: np.ndarray = np.array(a)
print(type(a_vec)) # <class 'numpy.ndarray'>
print(a_vec) # [1,2,3]

# Definiamo un vettore v e una matrice A
v = np.array([1, 1, 3, 2])
A = np.array([[1, 1, -1],
              [0, -1, 1]])

# Stampiamo la shape
print(f"La shape di v è: {v.shape}.") # (4,) monodimensionale righe 0 cols 4
print(f"La shape di A è: {A.shape}.") # (3,2) bidimensionale 2 righe 3 cols

# Creiamo un vettore
v = np.array([1, 2, 1.2])
print(v.dtype) # np.float64 (default)

# Creiamo lo stesso vettore in precisione singola
v = np.array([1, 2, 1.2], dtype=np.float32) # precisione singola (np.float32), doppia (np.float64) o anche mezza (np.float16)
print(v.dtype)

# Funzioni di numpy per la generazione di array (non partendo da array di python)
# np.linspace(a, b, n): Crea un vettore di lunghezza n, che contiene n elementi uniformemente distributi nel’intervallo , estremi inclusi.   
# np.arange(inizio, fine, passo): Simile alla funzione Python range. Crea un vettore che contiene tutti i numeri interi a partire da inizio, fino a fine-1, con passo fissato.
# np.zeros((m, n)): Crea una matrice di dimensione (m, n) di zeri. Chiaramente, per creare un vettore invece che una matrice, si utilizza la funzione np.zeros((m, )).
# np.ones((m, n)): Come prima, ma crea una matrice (o vettore) di 1.
# np.zeros_like(a): Crea una matrice o un vettore, della stessa dimensione di un altro array a. E’ equivalente a np.zeros(a.shape). Esiste l’equivalente np.ones_like(a).
# np.diag(v): Dato un vettore v di lunghezza n, costruisce una matrice diagonale di dimensione (n, n), la cui diagonale è v.
# ovvero 
# v = [1,2,3]
#
# v_diag = 1 0 0
#          0 2 0
#          0 0 3
#
#
# np.random.randn(m, n): Crea una matrice di dimensione (m, n) di numeri casuali distribuiti con distribuzione normale standard.
# np.random.rand(m, n): Uguale a prima, ma con valori estratti da una distribuzione uniforme nel dominio.

# Operazioni tra ndarray
a = np.array([1, -1, 0])
b = np.linspace(1, 3, 3) # array(1, 2, 3)

# Eseguiamo operazioni tra loro
s = a + b
d = a - b
p = a * b
f = a / b

print(f"a = {a}, b = {b} \nSomma: {s} \nDifferenza: {d} \nProdotto: {p} \nDivisione: {f}.")
# operazioni con val trigonometrici
x = np.linspace(0, 2*np.pi, 4)

# Calcoliamone i valori trigonometrici
print(f"sin(x) = {np.sin(x)}.")
print(f"cos(x) = {np.cos(x)}.")
print(f"tan(x) = {np.tan(x)}.")

# Ed esponenziale e logaritmo
print(f"e^x = {np.exp(x)}.")
print(f"ln(x) = {np.log(x + 1)}.")
print(f"log_10(x) = {np.log10(x + 1)}.")

# Definiamo una matrice A e un vettore x
A = np.array([[1, 1, 1], [0, -1, 0], [0, 0, 1]])
x = np.array([1, 0, 1])

# Calcoliamo y = Ax
y = A@x # prodotto riga-per-colonna tra matrici e vettori 
print(y) # [2 0 1]

# Definiamo due vettori classici
v = np.array([1, -1, 1])
w = np.array([0, 1, 1])
print(v.shape, w.shape) # Controlliamo che siano vettori classici

# Calcoliamone il prodotto scalare
print(v @ w)

## operanzioni logiche tra vettori
# Definiamo tre vettori casuali
a = np.random.rand(10)
b = np.random.rand(10)
c = np.random.rand(10)

# Generiamo il vettore booleano `v` che vale True quando un elemento di `a`
# è maggiore o uguale del corrispettivo elemento di `b`
v = a >= b
print(v) # [False False False False False False  True  True  True False]
# E il vettore `w`che vale True quando un elemento di `b` è maggiore o uguale
# del corrispettivo elemento di `c`
w = b >= c
print(w)  # [ True  True  True  True False  True  True False False False]
# Ora uniamoli con un operazione di `and` elemento per elemento
print(w & v) # [False False False False False False  True False False False]

# slicing array
# Definiamo un array
v = np.array([0, 1, -1, 2, 1, -1])

# Slicing
w = v[0:3]
print(w) # [0 1 -1]

# slicing di un array in base ai val di un altro (devono essere true o false)
# Creiamo un array di esempio
v = np.array([0, 1, -1, 2, 1, -1])
print(v)

# Definiamo un vettore booleano
b = np.array([True, True, False, True, False, False])
print(b)

# Slicing
print(v[b]) # [0 1 2]

# azzerare (=0) tutti i val negativi di un array
# Definiamo un vettore casuale
x = np.random.randn(8)
print(x)

# Proiettiamo sull'asse positivo
x[x < 0] = 0
print(x)


# Vediamo ad esempio come estrarre, da una matrice A di shape (3, 3), la sua sottomatrice principale di ordine 2, ovvero la sottomatrice di dimensione (2, 2) che si trova nell’angolo in alto a sinistra di A. 
# Creiamo la matrice
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing
B = A[:2, :2]
print(B)




