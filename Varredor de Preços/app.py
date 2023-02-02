'''O seu chefe precisa estar constantemente monitorando alguns sites para saber onde ele pode comprar pelo menor preço um determinado produto, sua responsabilidade e de fornecer uma planilha com os preços todos os dias, de pelo menos 3 sites para que ela possa decidir de onde comprar aquele determinado produto. O produto que preciso saber qual está mais barato é o abacate.'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from time import sleep

# abrir o navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# acessar o sitepreco1.netlify.app
driver.get('https://sitepreco1.netlify.app/')
sleep(5)
# encontrar onde está o acabate no site
precos_site_1 = driver.find_elements(By.XPATH,'//h6[@class="price_heading"]')
sleep(2)
# anotar o valor
preco_final_site_1 = precos_site_1[3].text.split(' ')[1]


driver.get('https://sitepreco2.netlify.app/')
sleep(5)
precos_site_2 = driver.find_elements(By.XPATH,"//h5")
sleep(2)
preco_final_site_2 = precos_site_2[3].text.split('$')[1]

driver.get('https://sitepreco3.netlify.app/')
sleep(5)
precos_site_3 = driver.find_elements(By.XPATH,'//div[@class="featured__item__text"]//h5')
sleep(2)
preco_final_site_3 = precos_site_3[2].text.split('$')[1]

# colocar o valor na planilha
with open('precos.csv','w',newline='',encoding='utf-8') as arquivo:
    arquivo.write(f'site,preço{os.linesep}')
    arquivo.write(f'https://sitepreco1.netlify.app/,{preco_final_site_1}{os.linesep}')
    arquivo.write(f'https://sitepreco2.netlify.app/,{preco_final_site_2}{os.linesep}')
    arquivo.write(f'https://sitepreco3.netlify.app/,{preco_final_site_3}{os.linesep}')