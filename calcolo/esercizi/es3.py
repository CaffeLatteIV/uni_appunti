import numpy as np

f = lambda x: x-np.cos(x)
df = lambda x: 1+np.cos(x)

def newton(ffun,dffun,x0,tol1,tol2,maxit):
    k=0
    x_new = x0
    while np.abs(ffun(x0))> tol1 and k< maxit:
        x_new = x0- (f(x0)/dffun(x0))
        if np.abs(x0-x_new) < tol2:
            break
        x0 = x_new
        k+=1
    return (x_new,k)

x0=0
tol1 = 1.e-6
tol2 = 1.e-5
maxit=100
sol = newton(f,df,x0,tol1,tol2,maxit)
print("Newton ", sol)
