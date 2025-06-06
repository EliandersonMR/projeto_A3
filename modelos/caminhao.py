class Caminhao:
    
    instancias = []
    def __init__(self, tipo, carga_maxima, limiteHoras):
        self.tipo = tipo
        self.carga_maxima = carga_maxima
        self.limiteHoras = limiteHoras
        self.entregas = []


        Caminhao.instancias.append(self)
        

    def adicionar_entrega(entrega):
        Caminhao.entregas.append(entrega)


    def getCaminhoes():
        return Caminhao.instancias
    

    def escolher_caminhao(qtd_carga):
        if qtd_carga > 500:
            return cGrande
            
        elif qtd_carga > 100:
            return cMedio
        else:
            return cPequeno



    def __repr__(self):
        return f"{self.tipo} - Carga máxima: {self.carga_maxima} - Limmite de horas de operação: {self.limiteHoras} - entregas: {self.entregas}"



cPequeno = Caminhao('Pequeno', 100, 10)
cMedio = Caminhao('Medio', 500, 8)
cGrande = Caminhao('Grande', 1000, 8)




