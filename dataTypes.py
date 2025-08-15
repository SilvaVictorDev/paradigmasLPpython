#Tipos Numéricos
inteiro = 10
flutuante = 5.5

#Operadores Numéricos 
soma = inteiro + flutuante
produto = inteiro * flutuante

#Tipo Booleano
verdadeiro = True
falso = False

#Exibindo os resultados
print("Soma:", soma) # Exibe a soma dos números
print("Produto:", produto) # Exibe o produto dos números
print("Verdadeiro:", verdadeiro) # Exibe o valor booleano True
print("Falso:", falso) # Exibe o valor booleano False

#Leitura de dados como strings
idade_str = "25"
altura_str = "1.75"

# Conversão de tipos
idade = int(idade_str)      # Convertendo string para intecrio
altura = float(altura_str)  # Convertendo string pata float

# Processamento usando os novos tipos de dados
mensagem = "Idade: " + str(idade) + ", Altura: " + str(altura)
# exibindo a mensagem
print(mensagem) # Exibe: Idade: 25, Altura: 1.75


# Solicita ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
 
# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3
 
# Mostra o resultado ao usuário
print(f"A média das notas é: {media:.2f}")

def soma_numeros(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Erro: entrada inválida")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return None
# Testes da função com números válidos
print(soma_numeros(2, 3)) # saída: 5
# Testes da função com números inválidos
print(soma_numeros("a", 3))
# Saída: Erro: entrada inválida
# Testes da função com outros tipos de dados
print(soma_numeros(True, 3))
# Saída: 4 (pois True é considerado 1 em Python)
# Testes da função comuma lista
print(soma_numeros([1, 2], 3))
# Saída: Erro: entrada inválida


#Atividade 4

"""
Você foi designado para desenvolver um programa que solicita ao usuário que insira três números: um número inteiro, um número de ponto flutuante e uma string representando um valor booleano (True ou False). Seu objetivo é converter esses valores para os tipos corretos e exibi-los ao usuário de forma formatada. Você deve seguir as seguintes instruções: 

    Solicite ao usuário que insira um número inteiro.
    Solicite ao usuário que insira um número de ponto flutuante.
    Converta os valores fornecidos pelo usuário para os tipos corretos (int, float e bool).
    Exiba os valores convertidos ao usuário de forma formatada, mostrando o tipo de cada valor.

Exemplo de saída:
```
Digite um número inteiro: 10
Digite um número de ponto flutuante: 3.14
Digite um valor booleano (True ou False): True 

Valores convertidos:
- Número inteiro: 10 (tipo: int)
- Número de ponto flutuante: 3.14 (tipo: float)
- Valor booleano: True (tipo: bool)"""

# Solicita ao usuário que insira um número inteiro
numero_inteiro = int(input("Digite um número inteiro: "))
# Solicita ao usuário que insira um número de ponto flutuante
numero_flutuante = float(input("Digite um número de ponto flutuante: "))
# Solicita ao usuário que insira um valor booleano
valor_booleano_str = bool(input("Digite um valor booleano (True ou False): "))
# Converte a string para um valor booleano

print("Número inteiro:", numero_inteiro, "(tipo:", type(numero_inteiro))
print("Número de ponto flutuante:", numero_flutuante, "(tipo:", type(numero_flutuante))
print("Valor booleano:", valor_booleano_str, "(tipo:", type(valor_booleano_str))
