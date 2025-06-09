from modelos.caminhao import Caminhao
from modelos.entrega import Entrega
from modelos.centro import CentroDistribuicao
from modelos.grafo import GrafoRotas
import sys
import time    
    


# Algoritmo de Dijkstra
def calcular_dijkstra(grafo, destino):
    distancias = {v: sys.maxsize for v in grafo}
    distancias[destino] = 0
    visitados = set()

    while visitados != set(distancias):
        vertice_atual = min(
            (v for v in grafo if v not in visitados),
            key=lambda v: distancias[v],
            default=None
        )

        if vertice_atual is None:
            break

        visitados.add(vertice_atual)

        for vizinho, peso in grafo[vertice_atual].items():
            nova_dist = distancias[vertice_atual] + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist

    return distancias

# Encontrar o centro de distribuição mais próximo
def centro_mais_proximo(caminhos):
    centros = CentroDistribuicao.getNomeCentros()
    valores = {c: caminhos[c] for c in centros if c in caminhos}
    menor_centro = min(valores, key=valores.get)
    return menor_centro, valores[menor_centro]

def main():
    grafo = GrafoRotas.getGrafo()

    print('Destinos Disponíveis:')
    GrafoRotas.exibeDestinos()

    entregas = []
    while True:
        try:
            destino = input('\nDigite o destino da para uma nova entrega (ou "sair" para calcular a rota): ').strip().lower()
            if destino == "sair":
                break
            if destino not in GrafoRotas.getDestinos():
                print('Destino não disponível.')
                continue
            
            peso = float(input('Peso da entrega em kg: '))
            prazo = float(input('Prazo para entrega em horas: '))
            
            entrega = Entrega(destino, peso, prazo)
            entregas.append(entrega)
        except Exception as e:
            print(f"Erro na entrada - dado invalido")

    inicio = time.time()

    for entrega in entregas:
        caminhos = calcular_dijkstra(grafo, entrega.destino)
        centro, distancia = centro_mais_proximo(caminhos)
        caminhao = Caminhao.escolher_caminhao(entrega.peso)
        caminhao.entregas.append(entrega)

        print(f"\nEntrega: {entrega.peso}kg para {entrega.destino} em {entrega.prazoEntrega}h")
        print(f"Caminho mais curto do centro '{centro}' até o destino: {distancia} km")
        print(f"Caminhão selecionado: {caminhao.tipo} (capacidade: {caminhao.carga_maxima}kg)")
        print(f"Entrega registrada: {centro} -> {entrega.destino}\n")

    fim = time.time()
    print(f"\nTempo total de execução: {fim - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
