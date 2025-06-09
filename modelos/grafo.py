class GrafoRotas:
    destinos = [
        'macapá',
        'amazonas',
        'rio branco',
        'altamira',
        'piaui',
        'salvador',
        'vitória',
        'curitiba',
        'porto alegre',
        'cuiaba'
    ]


        
    def getGrafo():

        grafo = {
                'macapá': {'centro de belém': 527, 'amazonas': 1688},
                'amazonas': {'macapá': 1688, 'altamira': 1264, 'rio branco': 760},
                'rio branco': {'amazonas': 760, 'altamira': 2248, 'cuiaba': 1966},
                'altamira': {'amazonas': 1264, 'rio branco': 2248, 'macapá': 1688, 'centro de belém': 816, 'piaui': 1370, 'centro de brasília': 1226, 'cuiaba': 1889},
                'centro de belém': {'macapá': 527, 'altamira': 816, 'piaui': 950, 'centro de brasília': 1007},
                'piaui': {'centro de belém': 950, 'altamira': 1370, 'centro de recife': 1170, 'salvador': 1040},
                'centro de recife': {'piaui': 1170, 'salvador': 806},
                'salvador': {'centro de recife': 806, 'piaui': 1040, 'vitória': 1088},
                'vitória': {'salvador': 1088, 'centro de brasília': 1244, 'centro de são paulo': 870},
                'centro de são paulo': {'vitória': 870, 'cuiaba': 1523, 'curitiba': 402},
                'curitiba': {'centro de são paulo': 402, 'centro de florianópolis': 315},
                'centro de florianópolis': {'curitiba': 315, 'porto alegre': 462},
                'porto alegre': {'centro de florianópolis': 462},
                'cuiaba': {'rio branco': 1966, 'altamira': 1889, 'centro de brasília': 1029, 'centro de são paulo': 1523},
                'centro de brasília': {'cuiaba': 1029, 'altamira': 1226, 'centro de belém': 1007, 'vitória': 1244}
        }


        return grafo
    

    def exibeDestinos():
        
        for destino in GrafoRotas.destinos:
            print(destino)

    def getDestinos():
        #return [destino.lower() for destino in GrafoRotas.destinos]
        return GrafoRotas.destinos






    
    

    
        


    