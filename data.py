import copy

def DataLic(cabecalho):
    try:
        data = copy.copy(cabecalho)
        data_fim = ''
        lista_data = ''
        for frases in data:
            if 'para conhecimento dos interessados' in frases:
                lista_data = frases.split()

        cortar = lista_data.index('realizar')
        del lista_data[:cortar]

        for palavra in range(len(lista_data)):
            data_fim = data_fim + ' ' + lista_data[palavra]

        return data_fim
    except:
        print('erro na data da licitação')
        return '---'
