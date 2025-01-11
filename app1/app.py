from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

navegador = webdriver.Chrome()

navegador.get("https://www.hashtagtreinamentos.com/?origemurl=75502579145&gad_source=1&gclid=CjwKCAiAp4O8BhAkEiwAqv2UqDhedX5JWfCYgd9HCiZ_EPV1OcERtvIo_l-tCbrKixPzyrOL20UcGBoCOjIQAvD_BwE")

navegador.maximize_window()

arrayButtons = navegador.find_elements('class name', 'header__titulo')

greenButton = navegador.find_element('class name', 'botao-verde')

greenButton.click()

#for button in arrayButtons:
 # if "Assinatura" in button.text:
  #  button.click()
  #  break """


abas = navegador.window_handles
navegador.switch_to.window(abas[1])

navegador.get("https://www.hashtagtreinamentos.com/curso-python")

InputName = navegador.find_element('id', 'firstname').send_keys("Adriano Tereza De Souza")
InputEmail = navegador.find_element("id", "email").send_keys("AdrianoSouzaa733@gmail.com")
InputPhone = navegador.find_element("id", "phone").send_keys("(31) 99523-2399")
greenButtonTwo = navegador.find_element("id", "_form_2475_submit")

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", greenButtonTwo)
 
wait = WebDriverWait(navegador, 10)
wait.until(EC.element_to_be_clickable(greenButtonTwo))

greenButtonTwo.click()

time.sleep(20)
