#Calcular el tiempo de ejecución de una función

from timeit import default_timer as timer

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

inicio = timer()
fibonacci(20)
fin = timer()

print(fin - inicio)