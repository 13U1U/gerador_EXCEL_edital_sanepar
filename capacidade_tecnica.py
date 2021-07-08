import copy

def CapTecnica(texto):
    try:
        cp_tec = copy.copy(texto)

        corte1 = cp_tec.index('14.3.2.3')
        cp_tec = cp_tec[corte1:]

        corte2 = cp_tec.index('\n')
        cp_tec = cp_tec[:corte2]

        cp_tec = cp_tec.replace('14.3.2.3', '')

        return cp_tec

    except:
        print('erro capacidade tecnica')
        return '---'
