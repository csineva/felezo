import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = "https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/salestax.html"
browser.get(URL)


# 1. teszteset
# a szükséges elemeket váktozókba mentjük, subtotalra kattintunk
subtotal = browser.find_element(By.ID, 'subtotal')
subtotal_btn = browser.find_element(By.ID, 'subtotalBtn')
subtotal_btn.click()
# ellenőrizzük, hogy a subtotal értéke az elvárt
assert subtotal.get_attribute('value') == '0.00'


# 2. testeset
# Select-el kiválasztjuk a listalelemet value alapon
select_item = Select(browser.find_element(By.ID, 'Proditem'))
select_item.select_by_value('4.95')


quantity = browser.find_element(By.ID, 'quantity')
billstate = browser.find_element(By.ID, 'billState')
quantity.send_keys('1')
billstate.click()

grandtotal_btn = browser.find_element(By.ID, 'gtotalBtn')
grandtotal_btn.click()

salestax = browser.find_element(By.ID, 'salestax')
gtotal = browser.find_element(By.ID, 'gtotal')

# a végösszeget ellenőrizzük
assert salestax.get_attribute('value') == '0.43'
assert gtotal.get_attribute('value') == '10.33'

