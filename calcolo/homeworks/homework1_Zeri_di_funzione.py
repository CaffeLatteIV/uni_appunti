import numpy as np
import matplotlib.pyplot as plt


def bisezione(f,a,b, tol, maxit):
    i: int = 0
    x: float = np.abs(a+b)/2
    while f(x) > tol and i < maxit:
        if a + x < 0:
            a = a
            b = x
        elif b + x < 0:
            a = x
            b = b
        else:
            print(f"Errore nella scelta dell'intervallo i: {i} x: {x}")
        x = np.abs(a+b)/2
        i = i+1
    return x, i

f = lambda x: np.pow(x,2) - np.cos(x)

