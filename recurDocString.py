# Função recursiva contagem regressiva

def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print("Acabou")
regressiva(10)

# Não Recursiva
for c in range(10, -1, -1):
    print(c)
print("Acabou")

# Função recursiva fatorial

def fatorial(n):
    """
    Calcula o fatorial de um número n.
    Exemplo: fatorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
print(fatorial(5))

# Não recursiva

def fatorial2(n):
    f = 1
    if n == 0 or n == 1:
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f
print(fatorial2(5))

# Docstring
# Determina o n-ésimo termo da sequência de Fibonacci

def fibonacci(n):
    if n ==1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
vfibo = fibonacci(10)
print(vfibo)
print(help(fibonacci))
