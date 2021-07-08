import copy


def ModoDisputa(cabecalho):
    try:
        disputa_fim = ''
        disputa = copy.copy(cabecalho)

        for frases in range(len(disputa)):
            if 'no modo de' in disputa[frases]:
                disputa_fim = str(disputa[frases])

        return disputa_fim

    except:
        print('erro no modo de disputa')
        return '---'
      
