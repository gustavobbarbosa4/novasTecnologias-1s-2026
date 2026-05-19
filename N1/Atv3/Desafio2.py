class Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"

    def alugar(self):
        self.status = "Alugado"

    def devolver(self):
        self.status = "Disponível"


class Locadora:
    def __init__(self):
        self.inventario = []
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for equipamento in self.inventario:
            if equipamento.id_equipamento == id_equipamento and equipamento.status == "Disponível":
                equipamento.alugar()
                custo = equipamento.preco_diaria * dias
                if nome_cliente in self.faturamento_por_cliente:
                    self.faturamento_por_cliente[nome_cliente] += custo
                else:
                    self.faturamento_por_cliente[nome_cliente] = custo
                return custo
        return None

    def equipamentos_disponiveis(self):
        return [equipamento.nome for equipamento in self.inventario if equipamento.status == "Disponível"]