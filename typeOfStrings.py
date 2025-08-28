# Delimitando string
s1 = 'aspas simples'
print(s1)
s2 = "aspas duplas"
print(s2)
s3 = '''aspas simples triplas'''
print(s3)
s4 = """aspas duplas triplas"""
print(s4)
print(s1, s2, s3, s4)

# Criando uma string
texto = "Olá, Mundo!"

# Acessando caracteres individuais (indexação)
primeiro_caractere = texto[0]
ultimo_caractere = texto[-1]

print('Primeiro caractere:', primeiro_caractere)
print('Último caractere:', ultimo_caractere)

# Fatiando strings (slicing)
sub_texto = texto[5:10]
print('Sub-texto (índices 5 a 9):', sub_texto)

# Concatenando strings
saudacao = "Olá"
nome = "Alice"
frase = saudacao + ", " + nome + "!"
print('Frase concatenada:', frase)

# Dividindo uma string em uma lista
lista_palavras = texto.split(", ")
print('Lista de palavras:', lista_palavras)

# Substituindo parte de uma string
texto_modificado = texto.replace(old="Mundo", new="Python")
print('Texto modificado:', texto_modificado)

# Convertendo para maiúsculas e minúsculas
texto_maiusculo = texto.upper()
texto_minusculo = texto.lower()
print('Texto em maiúsculas:', texto_maiusculo)
print('Texto em minúsculas:', texto_minusculo)

# Removendo espaços em branco (strip)
texto_com_espacos = "   Olá, Mundo!   "
texto_sem_espacos = texto_com_espacos.strip()
print('Texto sem espaços em branco:', '"' + texto_sem_espacos + '"')

# Verificando a presença de uma substring
if "Mundo" in texto:
    print('A palavra "Mundo" está presente no texto.')

# Formatação de strings (f-strings)
idade = 30
cidade = "São Paulo"
frase
frase_formatada = f'Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.'
print('Frase formatada:', frase_formatada)

# outro metodo de formatação
frase_formatada2 = 'Meu nome é {}, tenho {} anos e moro em {}.'.format(nome, idade, cidade)
print('Frase formatada (método format):', frase_formatada2)
