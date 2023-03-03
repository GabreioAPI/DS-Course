from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from getpass import getpass
from time import sleep


# Pedindo email e senha para logar
email = input('Digite seu email: ')
senha = getpass('Digite sua senha: ')


# Abrindo o navegador
chrome = webdriver.Chrome()

# Entrando em um link
in_portal = r'https://infinityschool.eadplataforma.com/login/'
chrome.get(in_portal)

# Logando
## Capturando os campos
email_entry = chrome.find_element(By.ID, 'email')
email_entry.send_keys(email)

senha_entry = chrome.find_element(By.ID, 'senha')
senha_entry.send_keys(senha)

## Clicando no botão de logar
butao_login = chrome.find_element(By.ID, 'btn_login')
butao_login.click()

sleep(10)