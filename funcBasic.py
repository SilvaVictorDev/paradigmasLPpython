# This program demonstrates basic function definitions and calls in Python.

def calcula_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC) dado peso e altura."""
    return peso / (altura ** 2)

peso = eval(input("Digite seu peso em kg: "))
altura = eval(input("Digite sua altura em metros: "))
calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)
print("Seu IMC é:", imc)


def taximetro(distancia, multipicador = 1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multipicador
    return valor

pagamento = taximetro(10)
print("O valor da corrida é:", pagamento)

# Exemple de função com variável local e global

def func1(x):
    x = 10
    print("Função func1 - x =", x)

def func2(x):
    x = 20
    print("Função func2 - x =", x)
    return x
vn = 0
print("Programa principal - vn = ", vn)
vn = func1(vn)
print("Programa principal - vn = ", vn)
vn = func2(vn)
print("Programa principal - vn = ", vn)
