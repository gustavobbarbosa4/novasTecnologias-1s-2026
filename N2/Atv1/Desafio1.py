import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

# médias por aluno
medias = np.mean(notas, axis=1)

# aluno com maior média
melhor_aluno = np.argmax(medias)

# normalização
media_colunas = np.mean(notas, axis=0)
std_colunas = np.std(notas, axis=0)

notas_normalizadas = (notas - media_colunas) / std_colunas

# aprovados
aprovados = medias >= 6.0
notas_aprovados = notas[aprovados]

print("Médias:", medias)
print("Melhor aluno:", melhor_aluno + 1)

print("\nNotas normalizadas:")
print(notas_normalizadas)

print("\nNotas dos aprovados:")
print(notas_aprovados)