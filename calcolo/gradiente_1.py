import numpy as np
import matplotlib.pyplot as plt
# potresti fare un notebook (si può su neovim?? BOH)
def GD(f, df, x0, alpha, maxit): # df può contenere la derivata (se n ==1), il gradiente (se n>1)
    """
    Implementazione metodo del gradiente
    """
    k=0

    while k<maxit:
        x = x0-alpha * df(x0)
        k=k+1
        x0=x

    return x,k

f = lambda x: (x-1)**2+np.exp(x) # f(x) = 2(x+1)^2 + e^x
df = lambda x: 2*(x-1)+np.exp(x) # f(x) = 4(x+1)+e^x
x0=0
x_true = 0.31492 # sarebbe un approssimazione di x*
maxit =200
alpha = 1.e-2
sol,numit = GD(f,df,x0,alpha,maxit)
print(f"soluzione calcolata {sol} in {numit} iterazioni")
print(f"errore {np.abs(x_true-sol)}")
# soluzione calcolata 0.5616172201126455 in 200 iterazioni
# errore 0.2466972201126455
# soluzione brutta

def GD_con_grafici(f, df, x0, alpha, maxit, x_true): # df può contenere la derivata (se n ==1), il gradiente (se n>1)
    errore = np.zeros((maxit,)) # vettore colonna con maxit righe e zero (in realtà una) colonna
    fun = np.zeros((maxit,)) # uso np.zeros cosi inizializzo in array più efficienti la lista
    """
    Implementazione metodo del gradiente
    """
    k=0
    errore[k] = np.abs(x_true-x0) # solo perchè non uso il gradiente
    fun[k]= f(x0)

    while k<maxit-1:
        x = x0-alpha * df(x0)
        k=k+1
        x0=x
        errore[k] = np.abs(x_true-x0) # solo perchè non uso il gradiente
        fun[k]= f(x0)
    return x,k, errore, fun

f = lambda x: (x-1)**2+np.exp(x) # f(x) = 2(x+1)^2 + e^x
df = lambda x: 2*(x-1)+np.exp(x) # f(x) = 4(x+1)+e^x
x0=0
x_true = 0.31492 # sarebbe un approssimazione di x*
maxit =200
alpha = 1.e-2
sol,numit, errore, fun= GD_con_grafici(f,df,x0,alpha,maxit, x_true)
print(f"soluzione calcolata {sol} in {numit} iterazioni")
print(f"errore {np.abs(x_true-sol)}")
plt.figure()
plt.plot(errore) # si può vedere che la diminuzione dell'errore non è lineare
plt.show()

# gradiente
def GD_con_grafici_gradiente(f, df, x0, alpha, maxit, x_true): # df può contenere la derivata (se n ==1), il gradiente (se n>1)
    errore = np.zeros((maxit,)) # vettore colonna con maxit righe e zero (in realtà una) colonna
    fun = np.zeros((maxit,)) # uso np.zeros cosi inizializzo in array più efficienti la lista
    grad = np.zeros((maxit,)) 
    """
    Implementazione metodo del gradiente
    """
    k=0
    errore[k] = np.abs(x_true-x0) # solo perchè non uso il gradiente
    fun[k]= f(x0)
    grad[k] = np.abs(df(x0))
    while k<maxit-1:
        x = x0-alpha * df(x0)
        k=k+1
        x0=x
        errore[k] = np.abs(x_true-x0) # solo perchè non uso il gradiente
        fun[k]= f(x0)
        grad[k] = np.abs(df(x0))
    return x,k, errore, fun,grad

f = lambda x: (x-1)**2+np.exp(x) # f(x) = 2(x+1)^2 + e^x
df = lambda x: 2*(x-1)+np.exp(x) # f(x) = 4(x+1)+e^x
x0=0
x_true = 0.31492 # sarebbe un approssimazione di x*
maxit =200
alpha = 1.e-2
# posso fermarmi se il gradiente è molto piccolo (es. 10^-4 o 10^-5) 
# oppure se la differenza tra i gradienti inizia a essere molto piccola
sol,numit, errore, fun, grad= GD_con_grafici_gradiente(f,df,x0,alpha,maxit, x_true)
print()
print(f"soluzione calcolata {sol} in {numit} iterazioni")
print(f"errore {np.abs(x_true-sol)}")
print(f"gradiente {grad}")
plt.figure()
plt.plot(errore) # si può vedere che la diminuzione dell'errore non è lineare
plt.show()

# backtracking 
def backtracking(f, df, x):
    alpha = 1
    c1 = 0.25
    rho = 1/2
    while f(x+alpha*df(x))> f(x) +c1*alpha+np.linalg.norm(df(x)) # f(x_k - alpha delta f(x_k)) <=  (x_k)- c_1 (delta f(x_k))^T delta f(x_k)
        alpha = rho +alpha
def GD_con_grafici_gradiente_backtracking(f, df, x0, maxit, x_true): # df può contenere la derivata (se n ==1), il gradiente (se n>1)
    """
    Implementazione metodo del gradiente
    """
    errore = np.zeros((maxit,)) # vettore colonna con maxit righe e zero (in realtà una) colonna
    fun = np.zeros((maxit,)) # uso np.zeros cosi inizializzo in array più efficienti la lista
    grad = np.zeros((maxit,)) 
    k=0
    alpha = backtracking(f,df,x0)
    errore[k] = np.abs(x_true-x0) # solo perchè non uso il gradiente
    fun[k]= f(x0)
    grad[k] = np.abs(df(x0))
    while k<maxit-1:
        x = x0-alpha * df(x0)
        k=k+1
        x0=x
        errore[k] = np.abs(x_true-x0) # solo perchè non uso il gradiente
        fun[k]= f(x0)
        grad[k] = np.abs(df(x0))
    return x,k, errore, fun,grad

f = lambda x: (x-1)**2+np.exp(x) # f(x) = 2(x+1)^2 + e^x
df = lambda x: 2*(x-1)+np.exp(x) # f(x) = 4(x+1)+e^x
x0=0
x_true = 0.31492 # sarebbe un approssimazione di x*
maxit =200
alpha = 1.e-2
# posso fermarmi se il gradiente è molto piccolo (es. 10^-4 o 10^-5) 
# oppure se la differenza tra i gradienti inizia a essere molto piccola
sol,numit, errore, fun, grad= GD_con_grafici_gradiente(f,df,x0,alpha,maxit, x_true)
print()
print(f"soluzione calcolata {sol} in {numit} iterazioni")
print(f"errore {np.abs(x_true-sol)}")
print(f"gradiente {grad}")
plt.plot(errore) # si può vedere che la diminuzione dell'errore non è lineare
