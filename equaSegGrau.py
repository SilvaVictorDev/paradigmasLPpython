# Este algoritmo calcula a solução de uma equação do segundo grau usando a biblioteca math.
import math

input_a = float(input("Digite o valor de a (coeficiente de x²): "))
input_b = float(input("Digite o valor de b (coeficiente de x): "))
input_c = float(input("Digite o valor de c (termo constante): "))

def equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        raiz = -b / (2*a)
        return f"A equação possui uma raiz real: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return f"A equação possui duas raízes reais: {raiz1} e {raiz2}"
