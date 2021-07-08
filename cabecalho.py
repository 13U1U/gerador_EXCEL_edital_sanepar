import copy


def CabecalhoTrado(texto):
    try:
        textoC2 = copy.copy(texto)
        valor_inicio = textoC2.index('N°')
        valor_fim = textoC2.index('CAPÍTULO I')

        cabecalho = textoC2[valor_inicio:valor_fim]
        cabecalho = cabecalho.replace('\n', ' ')
        cabecalho.split(',')

        return  cabecalho

    except:
        print('erro no cabeçalho')
        return '---'
