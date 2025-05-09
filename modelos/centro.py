class CentroDistribuicao:
    def __init__(self, nome: str):
        self.nome = nome
        self.estoque = 10000
        self.entregas = []

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)

    def __repr__(self):
        return f"{self.nome} - Estoque: {self.estoque} - Entregas: {len(self.entregas)}"
    