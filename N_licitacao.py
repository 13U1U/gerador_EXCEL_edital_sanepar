import copy

def NLicitacao(cabecalho):
    try:
        num_licitacao = ''
        ntext = copy.copy(cabecalho)

        for frases in range(len(ntext)):
            if 'Nº' in ntext[frases]:
                num_licitacao = str(ntext[frases])

        num_licitacao = num_licitacao.replace('Licitação', '')
        num_licitacao = num_licitacao.replace('Pública', '')
        num_licitacao = num_licitacao.replace('Nº', '')
        num_licitacao = num_licitacao.replace(' ', '')

        return num_licitacao

    except:
        print('erro no numero da licitação')
        return '---'
