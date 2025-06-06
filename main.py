from modelos.caminhao import Caminhao
from modelos.entrega import Entrega
from modelos.centro import CentroDistribuicao
from modelos.grafo import GrafoRotas
import sys

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

# Escolher o melhor caminhão baseado na quantidade de carga


def main():

    grafo = GrafoRotas.getGrafo()


    print('Destinos')
    #GrafoRotas.exibeDestinos()
    try:
        destino = str(input('Digite o destino da entrega: '))
        peso = float(input('Pedo da entrega em kg: '))
        prazo = float(input('Prazo para entrega em horas: '))

        entrega = Entrega(destino, peso, prazo)
        caminhao = Caminhao.escolher_caminhao(peso)

        caminhao.entregas.append(entrega)
    except:
        ...
    
    
    
    
    caminhos = calcular_dijkstra(grafo, destino)


    print("\nCaminhos calculados a partir do destino:")
    for k, v in caminhos.items():
        print(f"{k}: {v} km")

    centro, distancia = centro_mais_proximo(caminhos)
    print(f"\nCentro de distribuição mais próximo: {centro} ({distancia} km)")

    # Exemplo de entrega
    
    print(f"\nCaminhão selecionado: {caminhao.tipo} com capacidade de {caminhao.carga_maxima} unidades")

    
    print(f"\nEntrega criada: De {centro} para {entrega.destino}, "
          f"{entrega.peso} unidades, usando caminhão {caminhao.tipo}")

if __name__ == "__main__":
    main()
