from modelos.caminhao import Caminhao
from modelos.entrega import Entrega
from modelos.centro import CentroDistribuicao
from modelos.grafo import GrafoRotas
import sys

#if __name__ == "__main__":

    

# Função do algoritmo de Dijkstra
def calcular_dijkstra(grafo, origem):

  # Inicialização das distâncias com infinito, exceto a origem que é zero
  distancias = {v: sys.maxsize for v in grafo}
  distancias[origem] = 0

  # Conjunto de vértices visitados
  visitados = set()

  while visitados != set(distancias):
      # Encontra o vértice não visitado com menor distância atual
      vertice_atual = None
      menor_distancia = sys.maxsize
      for v in grafo:
          if v not in visitados and distancias[v] < menor_distancia:
              vertice_atual = v
              menor_distancia = distancias[v]

      # Marca o vértice atual como visitado
      visitados.add(vertice_atual)

      # Atualiza as distâncias dos vértices vizinhos
      for vizinho, peso in grafo[vertice_atual].items():
          if distancias[vertice_atual] + peso < distancias[vizinho]:
              distancias[vizinho] = distancias[vertice_atual] + peso

  # Retorna as distâncias mais curtas a partir da origem
  return distancias


def centroProximo(Caminhos):
    centros = 'Recife, Brasília, Salvador, Rio de Janeiro'
    valores = {}
    for chave, valor in Caminhos.items():
        if chave in centros:
            valores[chave] = valor
    

    menorChave = min(valores, key=valores.get)
    menorValor = valores[menorChave]
    print(menorChave, menorValor) 
    




# Definindo o grafo com as conexões e custos
grafo = {
    'Rio de Janeiro': {'A': 6, 'Brasília': 12},
    'Salvador': {'B': 5, 'Recife': 8},
    'Brasília': {'Rio de Janeiro': 12, 'C': 7, 'Salvador': 10},
    'Recife': {'Salvador': 8, 'D': 4},
    'A': {'Rio de Janeiro': 6, 'B': 3, 'C': 4},
    'B': {'A': 3, 'Salvador': 5, 'E': 6},
    'C': {'A': 4, 'Brasília': 7, 'D': 2},
    'D': {'C': 2, 'Recife': 4, 'E': 3},
    'E': {'B': 6, 'D': 3}
}

# Ponto de partida
origem = 'D'

# Chamando o algoritmo de Dijkstra para encontrar os caminhos mais curtos a partir de A
caminhos_mais_curto = calcular_dijkstra(grafo, origem)
print("-----------------------")
centroProximo(caminhos_mais_curto)
print("-----------------------")
