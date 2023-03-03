from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib.parse import quote


# Criando nosso navegador
driver = webdriver.Chrome()

# Conseguindo contatos
contatos = []

## Navegando a pagina
driver.get("https://dontpad.com/selenium_workshop")
sleep(1)

## Pegando os contatos do site
textarea = driver.find_element(By.CSS_SELECTOR, "textarea").get_attribute('value')

## Tratando os dados
text_contatos = textarea.split('\n')[7:]
for contato in text_contatos:
    nome, numero = contato.split(' - ')

    contatos.append({
        'nome': nome, 
        'numero': '+55' + numero
    })

# Enviando Mensagens
## Logando no seu whatsapp
driver.get('https://web.whatsapp.com/')
driver.maximize_window()

## Aguardando Logar
while driver.title in ('WhatsApp', 'WhatsApp Web'): pass # sleep(20) -> outra opção
sleep(3)
### OBS: Tem que ter mensagem que não foi vizualizada

## Enviando as mensagens
for contato in contatos:
    ### Criando a Mensagem
    mensagem = quote(f'Olá {contato["nome"]}! Seja muito bem-vindo(a) ao workshop de Selenium!')

    ### Abrindo o chat
    chat = f'https://web.whatsapp.com/send?phone={contato["numero"]}&text={mensagem}'
    driver.get(chat)
    sleep(8)

    ### Enviando a Mensagem
    text_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    msg_area = driver.find_element(By.XPATH, text_box_xpath)
    msg_area.send_keys(Keys.RETURN)
    sleep(2)

