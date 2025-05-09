class Entrega:
    def __init__(self, destino, prazo, carga):
        self.destino = destino
        self.prazo = prazo
        self.carga = carga

    def __repr__(self):
        return f"Entrega para {self.destino} - Prazo: {self.prazo} - Carga: {self.carga} unidades"
