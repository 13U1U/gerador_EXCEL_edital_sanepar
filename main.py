from web_scraper import WebScrap
# from web_driver import WebDriv
from PDF_to_string import PdfToString
from N_licitacao import  NLicitacao
from cabecalho import  CabecalhoTrado
from objeto import Objeto
from data import DataLic
from modo_de_disputa import ModoDisputa
from regime import Regime
from preco import PrecoText
from quadro_a import QuadroA
from capacidade_tecnica import CapTecnica

from time import sleep
import xlsxwriter


# Automação Web Para Fazer o Dowlond de todos os editais
LinksProcurar = WebScrap()
# WebDriv(LinksProcurar)


file = xlsxwriter.Workbook("Sanepar_Editais.xlsm")
excel = file.add_worksheet()


# adicionando ao excel
for numero_edital in range(len(LinksProcurar)):
    numero_edital += 1

    TextoStr = PdfToString(numero_edital)
    cabecalho = CabecalhoTrado(TextoStr)

    excel.write('A'+str(numero_edital), NLicitacao(TextoStr)) #numero da licitação
    excel.write('B'+str(numero_edital), Objeto(TextoStr)) # Objeto
    excel.write('C'+str(numero_edital), DataLic(cabecalho)) # Data entrega
    excel.write('D'+str(numero_edital), ModoDisputa(cabecalho)) #modo de disputa
    excel.write('E'+str(numero_edital), Regime(cabecalho)) #regime
    excel.write('F'+str(numero_edital), PrecoText(TextoStr)) # preço
    excel.write('G'+str(numero_edital), QuadroA(TextoStr)) # quadro A
    excel.write('H'+str(numero_edital), CapTecnica(TextoStr)) # capacidade tecnica

    sleep(0.2)


file.close()
