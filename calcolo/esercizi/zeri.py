import numpy as np  
import matplotlib.pyplot as plt

# zeri di funzione 1 f (x) = ln(x + 1) − x (g(x) = ln(x + 1))
f = lambda x: np.log(x+1) - x
g = lambda x: np.log(x+1)
x = np.linspace(-1,1)
print(f(-1))
plt.plot(x, f(x))
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True, which='both')
plt.show()
# metodo delle iterazioni
def bisezione(f,a,b,N):
    med = a+b/2
    if f(a)* f(b)>0:
        return None
    for i in range(0,N):
        med = a+b/2
        if f(a)* f(med)>0:
            a = med
        else:
            b = med

    return med;

a = -1
b = 1
N = 50
res = bisezione(f=f, a=a, b=b, N=N)
print(res)



