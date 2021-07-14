from selenium import webdriver
from time import sleep

def WebDriv(lista_links):

    navegador = webdriver.Chrome()

    cont = 0

    for editais in lista_links:
        cont += 1
        try:
            navegador.get(editais)
            navegador.find_element_by_xpath('//*[@id="wrdb_anexos_0"]').click()
            navegador.find_element_by_xpath('//*[@id="lbdownload"]').click()
            navegador.find_element_by_xpath('//*[@id="wbtn_semcadastro"]').click()
            sleep(1)
        except:
            try:
                navegador.get(lista_links[cont])
                navegador.find_element_by_xpath('//*[@id="wrdb_anexos_0"]').click()
                navegador.find_element_by_xpath('//*[@id="lbdownload"]').click()
                navegador.find_element_by_xpath('//*[@id="wbtn_semcadastro"]').click()
                sleep(1)
            except:
                try:
                    navegador.get(lista_links[cont])
                    navegador.find_element_by_xpath('//*[@id="wrdb_anexos_1"]').click()
                    navegador.find_element_by_xpath('//*[@id="lbdownload"]').click()
                    navegador.find_element_by_xpath('//*[@id="wbtn_semcadastro"]').click()
                except:
                    pass

    return
