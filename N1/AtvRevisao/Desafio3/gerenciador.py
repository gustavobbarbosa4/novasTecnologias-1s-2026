from usuario import Usuario

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def remover_usuario_por_id(self, id):
        for usuario in self.usuarios:
            if usuario.get_id() == id:
                self.usuarios.remove(usuario)
                print("Usuário removido com sucesso")
                return
        print("Usuário não encontrado")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado")
        else:
            for usuario in self.usuarios:
                print(usuario)