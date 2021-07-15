from urllib.request import urlopen
from bs4 import BeautifulSoup

# web scraper simples para achar todas a licitações
def WebScrap():
    try:
        html = urlopen('http://licitacoes.sanepar.com.br/SLI2A000.aspx')
        bs_sanepar = BeautifulSoup(html, 'html.parser')
    
        lista_links = []
    
        for link in bs_sanepar.find_all('a'):
    
            # Varendo todos os links da pagina
            if 'href' in link.attrs:
                linkagora = link.attrs['href']
    
                # Separando apenas os links de licitações
                if 'SLI2A100' in linkagora:
                    lista_links.append('http://licitacoes.sanepar.com.br/' + linkagora)
                    
        return lista_links
    
    except:
        print('erro no site da sanepar')
        return 'erro'
