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

limpar_dados = [usuarios]
limpos = []
usuarios_ativos = list(filter(
    lambda u: u["status_ativo"], usuarios
))

for usuario in usuarios:
    usuario = usuario["nome"].upper()
    limpos.append(usuario)

for usuario in usuarios:
    usuario = usuario["email"].lower()
   
for usuario in usuarios:
    print(f"{usuario["nome"]} | {usuario['email']}")