import numpy as np
import matplotlib.pyplot as plt


def bisezione(f,a,b, tol, maxit):
    if f(a) * f(b) >0:
        print("Il metodo di bisezione non è applicabile")
    i: int = 1
    x: float = (a+b)/2
    fxlist = [np.abs(f(x))]
    xlist = [x]
    while np.abs(f(x)) > tol and i < maxit:
        if f(a) * f(x) < 0:
            a = a
            b = x
        elif f(b) * f(x)  < 0:
            a = x
            b = b
        else:
            print(f"Errore nella scelta dell'intervallo i: {i} x: {x}")
            break
        x = (a+b)/2
        i = i+1
        fxlist.append(np.abs(f(x)))
        xlist.append(x)
    return x, i, np.array(fxlist)

def iterazioni_punto_fisso(f,g,x0,eps1,eps2,maxit):
    i:int = 0
    x: float = g(x0)
    while f(x) > eps1 and x-x0 > eps2 and i < maxit:
        x0 = x
        x = g(x0)
        i= i+1
# Es 2
def es2_bisezione():
    print("Esercizio 2 - Bisezione")
    f = lambda x: np.pow(x,2) - np.cos(x)
    arrayx = np.linspace(-3,3,50)
    a  = -2
    b =0.1
    tol = 1e-5
    maxit = 100
    x,i, fxlist = bisezione(f,a,b,tol,maxit)
    print(f"Bisezione intervallo [{a},{b}] i: {i},x: {x} f(x): {f(x)}")
    fig1, (ax1, ax2) = plt.subplots(2, figsize=(10, 4))
    ax1.set_title("Bisezione")
    ax1.spines['left'].set_position('zero')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.axvline(a,color="red", linestyle="--")
    ax1.axvline(b,color="red", linestyle="--")
    ax1.plot(arrayx, f(arrayx))
 
    xlist = np.linspace(-i, 0, i)
    ax2.set_title("Convergenza verso 0")
    ax2.spines['bottom'].set_position('zero')
    ax2.spines['left'].set_position('zero')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.plot(xlist,fxlist, color="green")

    a,b = (-0.5,1)
    x,i,fxlist = bisezione(f,a,b,tol,maxit)
    print(f"Bisezione intervallo [{a},{b}] i: {i},x: {x} f(x): {f(x)}")
    fig2, (ax3, ax4) = plt.subplots(2, figsize=(10, 4))
    ax3.set_title("Bisezione")
    ax3.spines['left'].set_position('zero')
    ax3.spines['bottom'].set_position('zero')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.axvline(a,color="red", linestyle="--")
    ax3.axvline(b,color="red", linestyle="--")
    ax3.plot(arrayx, f(arrayx))
 
    xlist = np.linspace(-i, 0, i)
    ax4.set_title("Convergenza verso 0")
    ax4.spines['bottom'].set_position('zero')
    ax4.spines['left'].set_position('zero')
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.plot(xlist,fxlist, color="green")

def es2_punto_fisso():
    fig1, (ax1, ax2) = plt.subplots(2, figsize=(10,4))

es2_bisezione()
#es2_punto_fisso()
plt.show()

