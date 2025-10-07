# funzioni lambda
# prendono in input uno o piu valori 
# quadrato = funzione
# lambda indica che ci sarà una lambda function
# x: l'input della funzione
# x**2 potenza di x
quadrato = lambda x: x**2
print(quadrato(5))

# *args
def somma(*args):
    r"Data una lista di valori in input, ne faccio la somma"
    print(f"somma di ${args}:", end="")

    res = 0
    for num in args:
        res+=num

    return res

print(somma(1,2,3,4,5))
print(somma(1,2,3))

