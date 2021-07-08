from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def PdfToString(numero_edital):
    try:
        def readPDF(pdfFile):
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            process_pdf(rsrcmgr, device, pdfFile)
            device.close()

            content = retstr.getvalue()
            retstr.close()
            return content

        pdfFile = urlopen(f"file:///C:/Users/matth/Downloads/EDITAL%20({numero_edital}).PDF")
        outputString = readPDF(pdfFile)
        pdfFile.close()
        print(numero_edital)
        return outputString

    # erro ainda a ser melhor trabalhado
    except:
        print('erro na leitura de pdf')
        def readPDF(pdfFile):
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            process_pdf(rsrcmgr, device, pdfFile)
            device.close()

            content = retstr.getvalue()
            retstr.close()
            return content

        pdfFile = urlopen(f"file:///C:/Users/matth/Downloads/EDITAL%20(1).PDF")
        outputString = readPDF(pdfFile)
        pdfFile.close()
        print(numero_edital)
        return outputString
