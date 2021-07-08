import copy

def Objeto(texto):
    try:
        objeto = copy.copy(texto)

        corte1 = objeto.index('2. OBJETO')
        corte2 = objeto.index('3. PRAZO DE EXECUÇÃO E PRAZO DE VIGÊNCIA DO CONTRATO')

        objeto = objeto[corte1:corte2]
        objeto = objeto.replace('\n','')
        objeto = objeto.replace('2. OBJETO ', '')

        return objeto

    except:
        return '---'
