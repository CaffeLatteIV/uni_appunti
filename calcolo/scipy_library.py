import  numpy as np
from scipy import optimize

f = lambda x: np.cos(x)-x
r = optimize.fsolve(f,-2)

print("zero calcolato", f)
print("valore funzione",f(r))

# metodo di bisezione

'''
codice base 
for i in range (N):
    c= (a+b)/2
    if f(a) * f(c) < 0:
        b=c
    else:
        a=c
'''
