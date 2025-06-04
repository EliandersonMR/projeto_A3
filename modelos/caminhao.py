class Caminhao:
    entregas = []
    instancias = []
    def __init__(self, tipo, carga_maxima, limiteHoras):
        self.tipo = tipo
        self.carga_maxima = carga_maxima
        self.limiteHoras = limiteHoras

        Caminhao.instancias.append(self)
        

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)



    
    


    def __repr__(self):
        return f"{self.tipo} - Carga máxima: {self.carga_maxima} - Limmite de horas de operação: {self.limiteHoras} - entregas: {self.entregas}"
