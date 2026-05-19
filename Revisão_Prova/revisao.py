# ===============================
# DADOS DE ENTRADA
# ===============================

notas_brutas = [
    {"aluno": "Ana", "materia": "Matematica", "nota": 8.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 6.0},
    {"aluno": "Beatriz", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Joao", "materia": "Historia", "nota": 7.5},
    {"aluno": "Mariana", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Pedro", "materia": "Matematica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Julia", "materia": "Quimica", "nota": 6.5},
    {"aluno": "Rafael", "materia": "Historia", "nota": 9.5},
    {"aluno": "Sofia", "materia": "Biologia", "nota": 10.0},
    {"aluno": "Ana", "materia": "Fisica", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 4.5},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 7.0},
    {"aluno": "Joao", "materia": "Quimica", "nota": 5.0},
    {"aluno": "Mariana", "materia": "Historia", "nota": 8.5},
    {"aluno": "Pedro", "materia": "Biologia", "nota": 6.0},
    {"aluno": "Lucas", "materia": "Matematica", "nota": 8.0},
    {"aluno": "Julia", "materia": "Fisica", "nota": 7.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Sofia", "materia": "Historia", "nota": 9.0},
    {"aluno": "Ana", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 3.0},
    {"aluno": "Beatriz", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Joao", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Mariana", "materia": "Quimica", "nota": 9.5},
    {"aluno": "Pedro", "materia": "Historia", "nota": 4.0},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 7.0},
    {"aluno": "Julia", "materia": "Matematica", "nota": 8.5},
    {"aluno": "Rafael", "materia": "Fisica", "nota": 6.0},
    {"aluno": "Sofia", "materia": "Quimica", "nota": 9.5},
    {"aluno": "Ana", "materia": "Matematica", "nota": 4.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 5.0},
    {"aluno": "Beatriz", "materia": "Historia", "nota": 7.5},
    {"aluno": "Joao", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 6.0},
    {"aluno": "Pedro", "materia": "Fisica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Julia", "materia": "Historia", "nota": 8.0},
    {"aluno": "Rafael", "materia": "Biologia", "nota": 7.5},
    {"aluno": "Sofia", "materia": "Matematica", "nota": 10.0},
    {"aluno": "Ana", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Carlos", "materia": "Historia", "nota": 6.5},
    {"aluno": "Beatriz", "materia": "Biologia", "nota": 9.5},
    {"aluno": "Joao", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Pedro", "materia": "Quimica", "nota": 6.0},
    {"aluno": "Lucas", "materia": "Historia", "nota": 8.5},
    {"aluno": "Julia", "materia": "Biologia", "nota": 9.0},
    {"aluno": "Rafael", "materia": "Matematica", "nota": 5.0},
    {"aluno": "Sofia", "materia": "Fisica", "nota": 8.5}
]


# FUNÇÃO PRINCIPAL

def gerar_boletins(dados):

    alunos = {}

    # Agrupar por aluno e matéria
    for registro in dados:

        aluno = registro["aluno"]
        materia = registro["materia"]
        nota = registro["nota"]

        if aluno not in alunos:
            alunos[aluno] = {}

        if materia not in alunos[aluno]:
            alunos[aluno][materia] = []

        alunos[aluno][materia].append(nota)

    boletins = {}
    ranking_aux = []

    # Calcular médias
    for aluno in alunos:

        medias_materias = {}

        for materia in alunos[aluno]:

            notas = alunos[aluno][materia][:]

            if len(notas) >= 3:
                while len(notas) > 2:
                    menor = min(notas)
                    notas.remove(menor)

            media = round(sum(notas) / len(notas), 2)

            medias_materias[materia] = media

        lista_medias = list(medias_materias.values())

        media_geral = round(sum(lista_medias) / len(lista_medias), 2)

        if media_geral >= 7:
            status = "Aprovado"
        elif media_geral >= 5:
            status = "Recuperacao"
        else:
            status = "Reprovado"

        boletins[aluno] = {
            "medias_disciplinas": medias_materias,
            "media_geral": media_geral,
            "status": status
        }

        ranking_aux.append((aluno, media_geral))

    ordenado = sorted(ranking_aux, key=lambda x: (-x[1], x[0]))

    ranking = []

    for item in ordenado:
        ranking.append(item[0])

    return {
        "boletins": boletins,
        "ranking": ranking
    }


# EXECUÇÃO

resultado = gerar_boletins(notas_brutas)

print("\n===== BOLETINS =====\n")

for aluno in resultado["boletins"]:

    dados = resultado["boletins"][aluno]

    print("Aluno:", aluno)

    print("Médias por disciplina:")

    for materia in dados["medias_disciplinas"]:
        print("  ", materia, ":", dados["medias_disciplinas"][materia])

    print("Média geral:", dados["media_geral"])
    print("Status:", dados["status"])

    print("------------------------")

print("\n===== RANKING DA TURMA =====\n")

posicao = 1
for aluno in resultado["ranking"]:
    print(posicao, "-", aluno)
    posicao += 1