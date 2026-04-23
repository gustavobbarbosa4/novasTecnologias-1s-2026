from usuario import Usuario
from gerenciador import GerenciadorUsuarios

gerenciador = GerenciadorUsuarios()

u1 = Usuario(1, "João", "joao@email.com")
u2 = Usuario(2, "Maria", "maria@email.com")

gerenciador.adicionar_usuario(u1)
gerenciador.adicionar_usuario(u2)

print("Lista de usuários:")
gerenciador.listar_usuarios()

u1.set_email("email_invalido")
u1.set_email("novo@email.com")

gerenciador.remover_usuario_por_id(1)

print("\nApós remoção:")
gerenciador.listar_usuarios()