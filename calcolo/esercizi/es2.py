import numpy as np
import matplotlib.pyplot as plt


# Metodo zero di funzione 2
f = lambda x: x-np.cos(x)
g= lambda x:np.cos(x)


x = np.linspace(-1,1,100)
y1= g(x )
y2 = x

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2,'r')
plt.show()
# posso fermarmi quando:
# abs(xk-gfun(xk)) < di tau (un valore molto piccolo)
# oppure abs(f(xk)) < di tau (un val molto piccolo) ### <-- cond su f, ovvero quando f(x) è vicino allo zero
# posso anche includere nelle due possibili cond che abs(xk+1-xk)< tau2 (ovvero, se la differenza tra i val di x è praticamente nulla, sono "arrivato")

def punto_fisso1(gfun, ffun, x0, tol1, tol2,maxit):
    k=0
    x_new = x0
    while np.abs(f(x0))>tol1 and k< maxit:
        x_new= gfun(x0)
        if np.abs(x_new-x0)< tol2:
            break
        x0= x_new
        k+=1
    return (x_new,k)

def punto_fisso2(gfun, ffun, x0, tol,maxit):
    k=0
    while np.abs(ffun(x0))>tol and k< maxit:
        x_new= gfun(x0)
        x0= x_new
        k+=1
    return (x0,k)

x0=0
tol1= 1.e-6
tol2= 1.e-5
maxit = 100
res = punto_fisso1(g,f,x0,tol1,tol2,maxit)
print("Punto fisso 1: ",res)
res = punto_fisso2(g,f,x0,tol1,maxit)
print("Punto fisso 2: ",res)
