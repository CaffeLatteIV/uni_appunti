import numpy as np
import matplotlib.pyplot as plt


f = lambda x: np.log(x+1)-x
g = lambda x: np.log(x+1)
def punto_fisso(f, g,tolf, tolx, x0, N):
    k: int = 0
    f_x_graph = [] 
    f_y_graph = []
    while np.abs(f(x0)) > tolf and k < N: 
        x = g(x0)
        f_x_graph.append(x)
        f_y_graph.append(np.abs(f(x)))
        if x0<= 0:
            print(f"{x} {k}")
        if np.abs(x0-x)<tolx:
            break
        x0 = x
        k += 1
    print(k)
    return x0, f_x_graph, f_y_graph 

x0: float = 4
tolx = 1.0e-6
tolf = 1.0e-5
N = 5_000
x = np.linspace(-1-1.0e-5,2,100)
y1 = f(x)
y2 = g(x)
plt.figure()
plt.plot(x,y1)
plt.plot(x,y2,'r')
res, f_x, f_y = punto_fisso(f,g,tolf, tolx, x0,N)
plt.plot(f_x,f_y,'g')
print(res)
plt.show()
