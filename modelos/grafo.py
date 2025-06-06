class GrafoRotas:
    destinos = [
            'macapá',
            'Amazonas',
            'Rio Branco',
            'Altamira',
            'piau',
            'Salvador',
            'Vitória',
            'curitiba',
            'Centro de Florianópolis',
            'Porto Alegre',
            'Cuiaba'
        ]

        
    def getGrafo():

        grafo = {
        'macapá': {'centro de Belém': 527, 'Amazonas': 1688},
        'Amazonas': {'macapá': 1688, 'Altamira': 1264, 'Rio Branco': 760},
        'Rio Branco': {'Amazonas': 760, 'Altamira': 2248, 'Cuiaba': 1966},
        'Altamira': {'Amazonas': 1264, 'Rio Branco': 2248, 'macapá': 1688, 'centro de Belém': 816, 'piau': 1370, 'centro de Brasília': 1226, 'Cuiaba': 1889},
        'centro de Belém': {'macapá': 527, 'Altamira': 816, 'piau': 950, 'centro de Brasília': 1007},
        'piau': {'centro de Belém': 950, 'Altamira': 1370, 'centro de Recife': 1170, 'Salvador': 1040},
        'centro de Recife': {'piau': 1170, 'Salvador': 806},
        'Salvador': {'centro de Recife': 806, 'piau': 1040, 'Vitória': 1088},
        'Vitória': {'Salvador': 1088, 'centro de Brasília': 1244, 'centro de São Paulo': 870},
        'centro de São Paulo': {'Vitória': 870, 'Cuiaba': 1523, 'curitiba': 402},
        'curitiba': {'centro de São Paulo': 402, 'Centro de Florianópolis': 315},
        'Centro de Florianópolis': {'curitiba': 315, 'Porto Alegre': 462},
        'Porto Alegre': {'Centro de Florianópolis': 462},
        'Cuiaba': {'Rio Branco': 1966, 'Altamira': 1889, 'centro de Brasília': 1029, 'centro de São Paulo': 1523},
        'centro de Brasília': {'Cuiaba': 1029, 'Altamira': 1226, 'centro de Belém': 1007, 'Vitória': 1244}
        }

        return grafo
    

    def exibeDestinos():
        
        for destino in GrafoRotas.destinos:
            print(destino)
    

    
    

    
        


    