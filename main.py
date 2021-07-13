from web_scraper import WebScrap
from web_driver import WebDriv #cometar essa parte caso não quera fazer o dowlond dos arquivos
from PDF_to_string import PdfToString
from N_licitacao import NLicitacao
from cabecalho import CabecalhoTrado
from objeto import Objeto
from data import DataLic
from modo_de_disputa import ModoDisputa
from regime import Regime
from preco import PrecoText
from quadro_a import QuadroA
from capacidade_tecnica import CapTecnica
from txt_dados import TxtAnalise

from time import sleep
import xlsxwriter


# Automação Web Para Fazer o Dowlond de todos os editais
LinksProcurar = WebScrap()
LinksNovos = TxtAnalise(LinksProcurar)
WebDriv(LinksNovos) #cometar essa parte caso não quera fazer o dowlond dos arquivos


# Medodos para ajeitar o excel
file = xlsxwriter.Workbook("Sanepar_Editais.xlsm")
excel = file.add_worksheet()

cell_format = file.add_format()
cell_format.set_text_wrap()
cell_format.set_align('center')
cell_format.set_align('vcenter')

excel.set_column(0, 0, 10)
excel.set_column(1, 1, 60)
excel.set_column(2, 4, 40)
excel.set_column(5, 6, 120)
excel.set_column(7, 7, 40)
excel.set_default_row(100)


# adicionando ao excel
for numero_edital in range(len(LinksProcurar)):
    numero_edital += 1

    TextoStr = PdfToString(numero_edital)
    cabecalho = CabecalhoTrado(TextoStr)

    excel.write('A'+str(numero_edital), NLicitacao(TextoStr), cell_format)    # numero da licitação
    excel.write('B'+str(numero_edital), Objeto(TextoStr), cell_format)        # Objeto
    excel.write('C'+str(numero_edital), DataLic(cabecalho), cell_format)      # Data entrega
    excel.write('D'+str(numero_edital), ModoDisputa(cabecalho), cell_format)  # modo de disputa
    excel.write('E'+str(numero_edital), Regime(cabecalho), cell_format)       # regime
    excel.write('F'+str(numero_edital), PrecoText(TextoStr), cell_format)     # preço
    excel.write('G'+str(numero_edital), QuadroA(TextoStr), cell_format)       # quadro A
    excel.write('H'+str(numero_edital), CapTecnica(TextoStr), cell_format)    # capacidade tecnica

    sleep(0.2)


file.close()
