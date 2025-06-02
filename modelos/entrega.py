class Entrega:
    def __init__(self, origem, destino, quantidade, caminhao):
        self.origem = origem
        self.destino = destino
        self.quantidade = quantidade
        self.caminhao = caminhao

    def __repr__(self):
        return f"Entrega para {self.destino} - Prazo: {self.prazo} - Carga: {self.carga} unidades"
