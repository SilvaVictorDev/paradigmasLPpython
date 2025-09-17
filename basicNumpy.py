# Utilizando o numpy pat calculat as raízes
# Importando o numpy
import numpy as np

# Função para calculat as raízes da equação de segundo grau

def calcular_raizes(a, b, c):
    # Coeficiente da equação
    coeficientes = [a, b, c]

    # Usando numpy.roots para calcular as raízes
    raizes = np.roots(coeficientes)
    return raizes
# Solicitando os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calculando as raízes
raizes = calcular_raizes(a, b, c)

# Imprimindo os resultados
print("As raízes da equação são: ", raizes[0], raizes[1])
