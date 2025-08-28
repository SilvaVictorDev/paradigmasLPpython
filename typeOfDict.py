#Criando um dicionário com alguns pares chave-valor
dicionario = {
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São Paulo'
}


# Acessando e imprimindo valores individuais usando chaves
nome = dicionario['nome']
idade = dicionario['idade']
cidade = dicionario['cidade']

print('Nome:', nome)
print('Idade:', idade)
print('Cidade:', cidade)

# Adicionando um novo par chave-valor ao dicionário
dicionario['profissão'] = 'Engenheira'
print('Dicionário após adicionar profissão:', dicionario)


# Modificando o valor associado a uma chave existente
dicionario['idade'] = 26
print('Dicionário após modificar idade:', dicionario)

# Removendo um par chave-valor usando a chave
del dicionario['cidade']
print('Dicionário após remover cidade:', dicionario)

# Acessando todas as chaves e valores do dicionário
chaves = dicionario.keys()
valores = dicionario.values()

print('Chaves do dicionário:', list(chaves))
print('Valores do dicionário:', list(valores))

# Iterando sobre os pares chave-valor do dicionário
print('Iterando sobre os pares chave-valor do dicionário:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')#Test

# Verificando se uma chave existe no dicionário
if 'nome' in dicionario:
    print('A chave "nome" existe no dicionário.')
else:
    print('A chave "nome" não existe no dicionário.')

# Usando o método get() para acessar valores com um valor padrão
profissao = dicionario.get('profissão', 'Desconhecida')
print('Profissão:', profissao)#Test

# Limpando todos os elementos do dicionário
dicionario.clear()
print('Dicionário após limpar todos os elementos:', dicionario)#Test
