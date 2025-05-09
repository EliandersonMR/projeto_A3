from modelos.caminhao import Caminhao
from modelos.entrega import Entrega
from modelos.centro import CentroDistribuicao
from modelos.grafo import GrafoRotas


if __name__ == "__main__":

    frota_de_caminhos = [
        Caminhao(tipo="Grande - Interestadual", carga_maxima=600, quantidade=8),
        Caminhao(tipo="Médio", carga_maxima=300, quantidade=10),
        Caminhao(tipo="Pequeno - Centro", carga_maxima=150, quantidade=20)
    ]

    # Criando os centros de distribuição
    centro_rio = CentroDistribuicao(nome="Rio de Janeiro")
    centro_sp = CentroDistribuicao(nome="São Paulo")

    # Criando entregas e centros
    entrega_niteroi = Entrega(destino="Niterói", prazo="mesmo", carga=100)
    entrega_campinas = Entrega(destino="Campinas", prazo="proximo", carga=250)

    centro_rio.adicionar_entrega(entrega_niteroi)
    centro_rio.adicionar_entrega(entrega_campinas)

    # Criando as rotas de entrega
    grafo_rotas = GrafoRotas()
    grafo_rotas.adicionar_rota(origem="Rio de Janeiro", destino="Niterói", distancia=20)
    grafo_rotas.adicionar_rota(origem="Rio de Janeiro", destino="Campinas", distancia=420)

    #frota de caminhões
    print("\n| ft de Caminhões |")
    for caminhao in frota_de_caminhos:
        print(caminhao)

    #centros de distribuição
    print("\n| Centros de Distribuição |")
    print(centro_rio)
    print(centro_sp)

    #rotas cadastradas
    print("\n| Rotas Cadastradas |")
    grafo_rotas.mostrar_rotas()
