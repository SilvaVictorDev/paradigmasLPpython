def diz_ola():
    print("Olá, mundo!")

diz_ola()

escolha = input("Escolha uma opção entre 1 ou 2: ")
if escolha == '1':
    def func1(x):
        return x + 1
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)
print(s)# No Python, funções podem ser definidas dentro de blocos condicionais.
# Isso permite criar funções específicas dependendo de certas condições.
# No entanto, é importante notar que a função só estará disponível
# dentro do escopo onde foi definida.