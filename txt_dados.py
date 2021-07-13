def TxtAnalise(lista):

    lista_avaliar = []

    with open('links_licitacao_sanepar.txt','r+') as arquivo:

        for links in lista:
            if links not in 'links_licitacao_sanepar.txt':

                arquivo.write(str(links)+'\n')
                lista_avaliar = lista_avaliar.append(links)


    return lista_avaliar
