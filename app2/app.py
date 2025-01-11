from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://demoqa.com/")

navegador.maximize_window()

element = navegador.find_element("class name", "avatar").click()

ButtonTextBox = navegador.find_element("id", "item-0").click()


InputUserName = navegador.find_element("id", "userName")
InputUserName.send_keys("Adriano Tereza De Souza")

time.sleep(1)

InputEmail = navegador.find_element("id", "userEmail")
InputEmail.send_keys("AdrianoSouzaa733@gmail.com")

time.sleep(1)

inputAddress = navegador.find_element("id", "currentAddress")
inputAddress.send_keys("Rua dos Curupiras (Pica Pau)")

time.sleep(1)

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",InputUserName)

inputPermanentAddress = navegador.find_element("id", "permanentAddress")
inputPermanentAddress.send_keys("Rua dos Curupiras ( Sem Pica Pau )")

time.sleep(1)

buttonSubmit = navegador.find_element("id", "submit")

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", buttonSubmit)

buttonSubmit.click()

time.sleep(1)

buttonCheckBox = navegador.find_element("id", "item-1").click()

time.sleep(1)

CheckBoxHome = navegador.find_element("class name", "rct-checkbox").click()

time.sleep(1)

RadioButton = navegador.find_element("id", "item-2").click()

time.sleep(1)

yesButton = navegador.find_element("class name", "custom-control").click()

time.sleep(1)

webTables = navegador.find_element("id", "item-3").click()

time.sleep(1)

addButton = navegador.find_element("id", "addNewRecordButton").click()

time.sleep(1)

InputName = navegador.find_element("id", "firstName").send_keys("Adriano")
InputLastName = navegador.find_element("id", "lastName").send_keys("Souza")
InputEmailR = navegador.find_element("id", "userEmail").send_keys("AdrianoSouzaa733@gmail.com")

time.sleep(1)

InputAge = navegador.find_element("id", "age").send_keys("19")
InputSalary = navegador.find_element("id", "salary").send_keys("25000")

time.sleep(1)

InputDepertament = navegador.find_element("id", "department").send_keys("I don't no about departament.")

time.sleep(1)

buttonSubmitR = navegador.find_element("id", "submit").click()

RemoveButton = navegador.find_element("id", "delete-record-1")

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", RemoveButton)

time.sleep(1)

RemoveButton.click()

RemoveButton2 = navegador.find_element("id", "delete-record-2").click()

time.sleep(1)

RemoveButton3 = navegador.find_element("id", "delete-record-3").click()
  
time.sleep(1)

ButtonForm = navegador.find_element("id", "item-4").click()

doubleClickButton = navegador.find_element("id", "doubleClickBtn")

doubleClickButton.click()
doubleClickButton.click()


#DoubleClickButtonWait = WebDriverWait(navegador, 10).until(
#  EC.element_to_be_clickable((By.ID, "doubleClickBtn"))
#)

# actionDoubleClick = ActionChains(navegador)

# actionDoubleClick.double_click(DoubleClickButtonWait).click().click().perform()

time.sleep(10)

