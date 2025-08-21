# This a example of structure for loops in Python While

palavra = input('Entre com uma palavra: \n')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

while True:
   print('loop')
   palavra = input('Entre com uma palavra:')
   if palavra == 'sair':
      break
print('Você digitou sair e agora está fora do laço')

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
               break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')