# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
# Acessando por índice (começa em 0)
print(frutas[0]) # maçã
print(frutas[-1]) # uva (último elemento)
# Fatiamento (slicing)
print(frutas[1:3]) # ['banana', 'laranja']
# Índices negativos percorrem a lista de trás para frente. frutas[-1] sempre retorna o último elemento.

# Adicionar
frutas.append(x) # Adiciona ao final

frutas.insert(i, x) # Insere na posição i

# Remover
frutas.remove(x) # Remove o valor x

frutas.pop(i) #Remove pelo índice
# frutas.pop(-1) Remove o ultimo item da lista

# Consultar
len(frutas) # Quantidade de itens

x in frutas # Verifica existência

# Ordenar
frutas.sort() # Ordena in-place

sorted(frutas)
# Retorna nova frutas
