def TxtAnalise(lista):
    lista_avaliar = []
    lista_antiga = []

    with open('links_licitacao_sanepar.txt', 'r+') as arquivo:
        for valor in arquivo:
            lista_antiga.append(valor.replace('\n',''))


        for links in lista:

            if str(links) in lista_antiga:
                pass

            else:
                arquivo.write(str(links) + '\n')
                lista_avaliar.append(links)


    return lista_avaliar
