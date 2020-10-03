#ciclo while
n=5
while n>0:
    print(n)
    n=n-1
print("Despegue!")

def esPrimo(n)->bool:
    i=1
    numeroDivisores = 0
    while(i<=n):
        if n % i == 0:
            numeroDivisores = numeroDivisores + 1
        i = i + 1
    if numeroDivisores == 2:
        resultado = True
    else:
        resultado = False
    return resultado

print(esPrimo(1))
print(esPrimo(2))
print(esPrimo(7))
print(esPrimo(10))
print(esPrimo(14))
print(esPrimo(28))

def PrimoDesde(m)->int:
    numero = m
    while not(esPrimo(numero)):
        numero = numero + 1
    return numero

print(PrimoDesde(0))