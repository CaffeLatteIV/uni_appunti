import numpy as np
import sys

x: float = 1.e05
'''
es (1+1/n)^n
'''


esp = np.logspace(0,16,17) # tutti i valori di n che voglio usare

for i in range(0,17):
    s = 1+(1/esp[i])**esp[i]
    print("i ", i, " err ", np.abs(s-np.exp(1))) # np.exp(1) è il val di nepero

# si può vedere la propagazione degli errori (errore cresce)

def precisione_di_macchina():
    epsilon = 1.0
    while 1.0 + epsilon/2.0 != 1.0:
        epsilon /= 2.0

    return epsilon
/2.0 != 1.0:
    epsilon /= 2.0

return epsilon

