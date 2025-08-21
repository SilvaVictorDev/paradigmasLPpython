# This is a example de structure for loops in Python

for item in range(2, 9, 3):
    print(item)

for numero in range(11):
    print(numero)

numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

nome = input("Entre com seu nome: \n")
for letra in nome:
    print(letra)

texto = "programação"
letra_para_contar = "a"
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1

print(f"A letra '{letra_para_contar}' aparece {contador} vezes na palavra '{texto}'.")

nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)

numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print(f'A soma de todos os números é {soma}')

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    quadrado = numero ** 2
    print(f'O quadrado de {numero} é {quadrado}')