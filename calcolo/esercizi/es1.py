import numpy as np
import matplotlib.pyplot as plt


# metodo di bisezione
a=-1;b=2
x = np.linspace(a,b,100)
y = x - np.cos(x)
plt.figure()
plt.plot(x,y)

y1= np.zeros(len(x))
plt.plot(x,y1,'r')
plt.show()

N=150
f = lambda x: x-np.cos(x) 

def bisezione(fun, a,b,N):
    for i in range(N):
        c = (a+b)/2
        if(fun(a)*fun(c)>= 0):
            a=c
        else:
            b=c
    return c

sol = bisezione(f,a,b,N)
print("sol bisezione ", sol)
