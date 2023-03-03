from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

'''
    https://chromedriver.chromium.org/downloads
    davi14007@gmail.com
'''
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get(r'https://infinityschool.eadplataforma.com/login/')


Xpath_email = '//*[@id="email"]'
Xpath_password = '//*[@id="senha"]'
Xpath_enter = '//*[@id="btn_login"]'

email = 'Exemplomail@gmail.com'
password = '123321'

email_box = navegador.find_element(By.XPATH, Xpath_email)
email_box.send_keys(email)

password_box = navegador.find_element(By.XPATH, Xpath_password)
password_box.send_keys(password)

enter_box = navegador.find_element(By.XPATH, Xpath_enter)
enter_box.click()
sleep(10)