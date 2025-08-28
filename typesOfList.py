# Criando uam lista com alguns elementos
lista = [10, 20, 30, 40, 50]

# Acessando elementos da lista
primeiro_elemento = lista[0]
segundo_elemento = lista[1]

# Imprimindo os elementos acessados
print('O primeiro elemento da lista é:', primeiro_elemento)
print('O segundo elemento da lista é:', segundo_elemento)

# Adicionando um eleento ao final da lista
lista.append(60)
print('Lista após adicionar 60:', lista)

# Inserindo um elemento em uma posição específica
lista.insert(index=2, object=25) #  Inserindo o 25 na posição 2
print('Lista após inserir 25 na posição 2:', lista)

# Removendo um elemento da lista
lista.remove(40) # Removendo o primeiro valor 40 encontrado
print('Lista após remover 40:', lista)

# Removendo o último elemneto da lista
ultimo_elemento = lista.pop()
print('Elemento removido com pop():', ultimo_elemento)
print('Lista após remover o último elemento:', lista)

# Acessando um subgrupo da lista (fatiamento)
sub_lista = lista[1:4] # Elementos do índice 1 ao 3
print('Sub-lista do índice 1 ao 3:', sub_lista)

# Ordenando a lista
lista.sort()
print('Lista ordenada:', lista)

# Iterando sobre os elementos da lista
print('Iterando sobre os elementos da lista:')
for elemento in lista:
    print(elemento)

# Tuplas

tupla_heterogenea = (1, "Olá"), 3.14, [10, 20, 30], {"chave": "valor"}
print("inteiro: ", tupla_heterogenea[0])
print("String: ", tupla_heterogenea[1])
print("Float: ", tupla_heterogenea[2])
print("Lista: ", tupla_heterogenea[3])
print("Dicionário: ", tupla_heterogenea[4])

# Modificando a lista dentro da tupla
tupla_heterogenea[3].append(40)
print("Tupla após modificar a lista dentro dela: ", tupla_heterogenea)

# Acessando um valor no dicionário dentro da tupla
valor_chave = tupla_heterogenea[4]["chave"]

# Iterando sobre a tupla impprimindo os tipos de elemento
for elemento in tupla_heterogenea:
    print(f'Elemento: {elemento}, Tipo: {type(elemento)}')

    