class CentroDistribuicao:
    def __init__(self, nome: str):
        self.nome = nome
        self.estoque = 10000
        

    def __repr__(self):
        return f"{self.nome} - Estoque: {self.estoque}"
    