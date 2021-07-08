import copy


def PrecoText(texto):
     try:
        preco = copy.copy(texto)
        corte1 = preco.index('4. PREÇO')
        corte2 = preco.index('5. RECURSOS FINANCEIROS')

        preco = preco[corte1:corte2]

        preco = preco.replace('\n', '')

        return preco

     except:
        print('erro no texto')
        return '---'
