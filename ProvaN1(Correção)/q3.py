# Função que calcula a soma dos elementos da diagonal principal de uma matriz quadrada.
# Recebe uma matriz representada como uma lista de listas, onde cada sublista é uma linha da matriz.
# Assume que a matriz é quadrada (mesmo número de linhas e colunas) para evitar erros de índice.
# Retorna a soma dos elementos onde o índice da linha é igual ao índice da coluna (diagonal principal).
def soma_diagonal_principal(matriz):
    # Inicializa a variável 'soma' com 0, que será usada para acumular a soma dos elementos da diagonal.
    soma = 0
    # Usa um loop 'for' para iterar sobre os índices de 0 até o tamanho da matriz (len(matriz)).
    # O método len() retorna o número de elementos em uma sequência, aqui usado para obter o número de linhas (e colunas, assumindo quadrada).
    # range(len(matriz)) gera uma sequência de números de 0 até len(matriz)-1, permitindo acessar cada linha.
    for i in range(len(matriz)):
        # Acessa o elemento na posição [i][i] da matriz, que é o elemento da diagonal principal para o índice i.
        # Soma esse elemento à variável 'soma' usando o operador +=, que é uma forma abreviada de soma = soma + matriz[i][i].
        soma += matriz[i][i]
    # Após processar todos os elementos da diagonal, retorna o valor total acumulado em 'soma'.
    return soma

# Exemplo de uso: Define uma matriz 3x3 como uma lista de listas, onde cada sublista representa uma linha.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Chama a função 'soma_diagonal_principal' passando a matriz como argumento e armazena o resultado na variável 'resultado'.
resultado = soma_diagonal_principal(matriz)
# Imprime o resultado usando uma f-string (formatação de string), que permite inserir variáveis diretamente na string.
# O método print() é usado para exibir a mensagem no console, incluindo a soma calculada (1 + 5 + 9 = 15 neste exemplo).
print(f"A soma dos elementos da diagonal principal e: {resultado}")