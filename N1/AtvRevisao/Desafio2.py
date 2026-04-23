transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licencas", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licencas", 150.00)
]

categorias = set()

for transacao in transacoes:
    categorias.add(transacao[1])

print("Categorias unicas:")
print(categorias)

totais = {}

for transacao in transacoes:
    categoria = transacao[1]
    valor = transacao[2]

    if categoria in totais:
        totais[categoria] += valor
    else:
        totais[categoria] = valor

print("Total gasto por categoria:")
print(totais)