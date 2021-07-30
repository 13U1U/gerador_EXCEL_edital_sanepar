import copy


def Regime(cabecalho):
    try:
        regime_fim = ''

        regime = copy.copy(cabecalho)
        regimelis = str(regime[-1]).split()
        regime_fim = regime_fim + str(regimelis[-3]) + ' ' + str(regimelis[-2]) + ' ' + str(regimelis[-1])

        return regime_fim

    except:
        print('erro no regime')
        return '---'
