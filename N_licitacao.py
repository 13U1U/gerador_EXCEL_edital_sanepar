import copy


def NLicitacao(texto):
    try:
        text_n = copy.copy(texto)
        LPdf = text_n.split()
    
        valorN = LPdf.index('N°')
        del LPdf[:valorN+1]
    
        num_licitacao =  LPdf[0]
    
        return num_licitacao
    
    except:
        print('erro no numero da licitação')
        return '---'
