# Este algotitmo encontra o maior elemento em uma lista usando recursão.

lista = [1,2,3,4,5,6,7,8,9,10]

def maior_elemento_recursivo(lista, n):
    if n == 1:
        return lista[0]
    else:
        max_anterior = maior_elemento_recursivo(lista, n - 1)
        return max(max_anterior, lista[n - 1])
print(maior_elemento_recursivo(lista, len(lista)))

"""
def encontrar_maior_elemento_nao_recursivo(lista):

  Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.

  Args:
    lista: A lista de números inteiros.

  Returns:
    O maior elemento da lista.
  

  if len(lista) <= 1:
    # Caso base: se a lista tiver no máximo 1 elemento, ele é o maior
    return lista[0]

  maior_elemento = lista[0]
  for numero in lista[1:]:
    if numero > maior_elemento:
      maior_elemento = numero

  return maior_elemento

# Exemplo de uso
lista_exemplo = [7, 2, 5, 9, 4, 3, 6]
maior_elemento = encontrar_maior_elemento_nao_recursivo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")def encontrar_maior_elemento_nao_recursivo(lista):
  
  Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.

  Args:
    lista: A lista de números inteiros.

  Returns:
    O maior elemento da lista.
  

  if len(lista) <= 1:
    # Caso base: se a lista tiver no máximo 1 elemento, ele é o maior
    return lista[0]

  maior_elemento = lista[0]
  for numero in lista[1:]:
    if numero > maior_elemento:
      maior_elemento = numero

  return maior_elemento

# Exemplo de uso
lista_exemplo = [7, 2, 5, 9, 4, 3, 6]
maior_elemento = encontrar_maior_elemento_nao_recursivo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")
"""