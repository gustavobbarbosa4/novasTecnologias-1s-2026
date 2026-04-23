usuarios = [
    {"nome": "Gustavo", "email": "gustavobbarbosa4@gmail.com", "status_ativo": True},
    {"nome": "MAriA", "email": "mariazinha@gmail.com", "status_ativo": False},
    {"nome": "IsaQue", "email": "ISAquinho@gmail.com", "status_ativo": True},
    {"nome": "joao", "email": "jaozao@gmail.com", "status_ativo": True},
    {"nome": "David", "email": "davidzinho123@gmail.com", "status_ativo": False},
    {"nome": "Yago", "email": "YAgueira@gmail.com", "status_ativo": False},
    {"nome": "guiLherme", "email": "guilherme616@gmail.com", "status_ativo": True},
    {"nome": "Bruna", "email": "bruninha@gmail.com", "status_ativo": True}
]

def limpar_dados(lista):
    usuarios_ativos = list(filter(lambda u: u["status_ativo"] == True, lista))
    limpos = []
    
    for usuario in usuarios_ativos:
        usuario["nome"] = usuario["nome"].upper()
        usuario["email"] = usuario["email"].lower()
        limpos.append(usuario)
    
    return limpos

resultado = limpar_dados(usuarios)

for usuario in resultado:
    print(f"{usuario['nome']} | {usuario['email']}")