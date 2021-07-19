import copy


def cabecalhotrado(texto):
    try:
        textoc2 = copy.copy(texto)
        valor_inicio = textoc2.index('Companhia')
        valor_fim = textoc2.index('CAPÍTULO I')

        cabecalho = textoc2[valor_inicio:valor_fim]
        cabecalho = cabecalho.replace('\n', ' ')
        cabecalho = cabecalho.split(',')

        return cabecalho

    except:
        print('erro no cabeçalho')
        return '---'
