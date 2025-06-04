class Entrega:
    def __init__(self, destino, peso, prazoEntrega):
        self.destino = destino
        self.peso = peso
        self.prazoEntrega = prazoEntrega

    def __repr__(self):
        return f"Entrega para {self.destino} - Prazo: {self.prazo} - Carga: {self.peso}kg"
