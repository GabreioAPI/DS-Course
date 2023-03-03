from selenium import webdriver
from selenium.webdriver.common.by import By
import os


# Abrindo o navegador
chrome = webdriver.Chrome()

# Entrando em um link
in_portal = r'https://infinityschool.com.br/'
chrome.get(in_portal)

# Capturando os elementos
seletor_css = 'div.elementor-widget-wrap a'
elementos_cursos = chrome.find_elements(By.CSS_SELECTOR, seletor_css)

# Tratando a saida
cursos_infinity = [element.text for element in elementos_cursos]
cursos_infinity = list(filter(lambda curso: curso not in ['', 'CONHEÇA MAIS'], cursos_infinity))
print(cursos_infinity)

if os.path.isfile('cursos.txt'):
    os.remove('cursos.txt')

with open('cursos.txt', 'w') as file:
    file.write('Cursos da Infinity: \n\n')
    for curso in cursos_infinity:
        file.write(f'- {curso}\n')