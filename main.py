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
    centros = ['centro de Recife', 'centro de Brasília', 'centro de São Paulo', 'centro de Belém', 'Centro de Florianópolis']
    valores = {c: caminhos[c] for c in centros if c in caminhos}
    menor_centro = min(valores, key=valores.get)
    return menor_centro, valores[menor_centro]

# Escolher o melhor caminhão baseado na quantidade de carga
def escolher_caminhao(qtd_carga):
    if qtd_carga > 300:
        return Caminhao('Grande', 600, qtd_carga)
    elif qtd_carga > 150:
        return Caminhao('Médio', 300, qtd_carga)
    else:
        return Caminhao('Pequeno', 150, qtd_carga)

def main():

    
   
    grafo = GrafoRotas.getGrafo()
    destino = 'Porto Alegre'
    caminhos = calcular_dijkstra(grafo, destino)


    print("\nCaminhos calculados a partir do destino:")
    for k, v in caminhos.items():
        print(f"{k}: {v} km")

    centro, distancia = centro_mais_proximo(caminhos)
    print(f"\nCentro de distribuição mais próximo: {centro} ({distancia} km)")

    # Exemplo de entrega
    qtd_carga = 280
    caminhao = escolher_caminhao(qtd_carga)
    print(f"\nCaminhão selecionado: {caminhao.tipo} com capacidade de {caminhao.carga_maxima} unidades")

    entrega = Entrega(centro, destino, qtd_carga, caminhao)
    print(f"\nEntrega criada: De {entrega.origem} para {entrega.destino}, "
          f"{entrega.quantidade} unidades, usando caminhão {entrega.caminhao.tipo}")

if __name__ == "__main__":
    main()
