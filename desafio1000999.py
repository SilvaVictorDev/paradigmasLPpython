"""Faça um programa em Python que mostre os números entre 1000 e 9999
cuja raiz quadrada seja igual à soma dos números formados pelos dois
algarismos menos significativos e pelos dois algarismos mais significativos.
 Dica: existem três números que atendem a condição."""

for num in range(1000, 10000):
    menor = num % 100 # obtém os dois algarismos menos significativos
    maior = num // 100 # obtém os dois algarismos mais significativos
    raiz  = (menor + maior)

    if (raiz * raiz) == num: # verifica se a raiz ao quadrado é igual ao número testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("Terminou")
print('saiu', num)

#Otimizando o código

for raiz in range(32, 100): # raiz quadrada de 1000 é 31.62 e de 9999 é 99.99
    num = raiz * raiz # calcula o número a partir da raiz
    menor = num % 100 # obtém os dois algarismos menos significativos
    maior = num // 100 # obtém os dois algarismos mais significativos

    if (menor + maior) == raiz: # verifica se a soma dos algarismos é igual à raiz
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("Terminou")
print('saiu', raiz)
