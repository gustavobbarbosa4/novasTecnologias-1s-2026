celular = {
    "nome": "Samsung",
    "preco": 1500.00,
    "quantidade": 2
}

monitor = {
    "nome": "AOC",
    "preco": 1200.00,
    "quantidade": 2
}

teclado = {
    "nome": "Royal Kludge",
    "preco": 500.00,
    "quantidade": 3
}

mouse = {
    "nome": "Atack Shark",
    "preco": 200.00,
    "quantidade": 0
}

produtos = [celular, monitor, teclado, mouse]
produtosCaros = []

total = 0

for produto in produtos:
    total += (produto["preco"] * produto["quantidade"]) 
    if produto["preco"] > 500:
        produtosCaros.append(produto)
        
emFalta = [produto["nome"] for produto in produtos if produto["quantidade"] == 0 ]

print(f"\nValor total em estoque: ${total:.2f}")

print(f"\nProdutos acima de 500:")

for produto in produtosCaros:
    valor = produto["preco"] * produto["quantidade"] 
    print(f"- {produto['nome']} | Quantidade: {produto['quantidade']} | Valor: {valor}")

print(f"\nProdutos em falta:")
for nome in emFalta:
    print(f"- {nome}")
