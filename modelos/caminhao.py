class Caminhao:
    def __init__(self, tipo, carga_maxima, quantidade):
        self.tipo = tipo
        self.carga_maxima = carga_maxima
        

    def __repr__(self):
        return f"{self.tipo} - Carga máxima: {self.carga_maxima} "

    