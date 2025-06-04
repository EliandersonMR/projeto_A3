class Caminhao:
    def __init__(self, tipo, carga_maxima, limiteHoras, entregas):
        self.tipo = tipo
        self.carga_maxima = carga_maxima
        self.limiteHoras = limiteHoras
        self.entregas = []

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)


    def __repr__(self):
        return f"{self.tipo} - Carga máxima: {self.carga_maxima} - Limmite de horas de operação: {self.limiteHoras} - entregas: {self.entregas}"
