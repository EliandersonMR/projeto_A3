class GrafoRotas:
    def __init__(self):
        self.rotas = {}

    def adicionar_rota(self, origem, destino, distancia):
        if origem not in self.rotas:
            self.rotas[origem] = {}
        if destino not in self.rotas:
            self.rotas[destino] = {}
        self.rotas[origem][destino] = distancia
        self.rotas[destino][origem] = distancia

    def mostrar_rotas(self):
        for origem, destinos in self.rotas.items():
            print(f"\n{origem} ->")
            for destino, distancia in destinos.items():
                print(f"   {destino}: {distancia} km")
    