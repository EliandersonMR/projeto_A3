class CentroDistribuicao:
    instancias = []
    def __init__(self, nome: str):
        self.nome = nome
        self.estoque = 10000

        CentroDistribuicao.instancias.append(self)
        

    def getNomeCentros():
        return [centro.nome for centro in CentroDistribuicao.instancias]

    def __repr__(self):
        return f"{self.nome} - Estoque: {self.estoque}"
    

c1 = CentroDistribuicao('centro de brasília')
c2 = CentroDistribuicao('centro de são paulo')
c3 = CentroDistribuicao('centro de recife')  
c4 = CentroDistribuicao('centro de belém')
c5 = CentroDistribuicao('centro de florianópolis')

