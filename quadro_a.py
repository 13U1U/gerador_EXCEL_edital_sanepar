import copy

def QuadroA(texto):
    try:
        qA = copy.copy(texto)

        corte1 = qA.index('QUADRO A')
        corte2 = qA.index('14.3.2.3.1')

        qA = qA[corte1:corte2]

        qA = qA.replace('\n', '')
        qA = qA.replace('QUADRO A', '')
        qA = qA.replace('\uf0b7', '')

        return qA

    except:
        print('erro no quadro A')
        return '---'
      
