# Função que encontra o aluno com a melhor nota em um dicionário de notas de alunos.
# Recebe um dicionário onde as chaves são os nomes dos alunos (strings) e os valores são as notas (números).
# Retorna uma tupla contendo o nome do aluno com a maior nota e a própria nota.
def melhor_aluno(notas_alunos):
    # Inicializa a variável 'melhor_nota' com -1, um valor baixo para garantir que qualquer nota real seja maior.
    # Isso serve como ponto de partida para comparações, assumindo que notas são positivas.
    melhor_nota = -1
    # Inicializa 'melhor_aluno' como uma string vazia, que será atualizada quando encontrarmos o primeiro aluno.
    melhor_aluno = ""

    # Itera sobre os pares chave-valor do dicionário 'notas_alunos' usando o método .items().
    # O método .items() retorna uma visão dos pares (chave, valor) do dicionário, permitindo acesso simultâneo ao nome do aluno e sua nota.
    for aluno, nota in notas_alunos.items():
        # Verifica se a nota atual é maior que a melhor nota encontrada até agora.
        # Se for, atualiza as variáveis para refletir o novo melhor aluno.
        if nota > melhor_nota:
            # Atualiza 'melhor_nota' com a nova nota mais alta.
            melhor_nota = nota
            # Atualiza 'melhor_aluno' com o nome do aluno correspondente.
            melhor_aluno = aluno

    # Após verificar todos os alunos, retorna uma tupla com o nome do melhor aluno e sua nota.
    # Se o dicionário estiver vazio, retorna ("", -1), mas assume-se que há pelo menos um aluno.
    return melhor_aluno, melhor_nota