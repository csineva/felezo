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

URL = "https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/bmi.html"
browser.get(URL)


# az input elemeket változóba mentjük
height = browser.find_element(By.ID, 'height')
weight = browser.find_element(By.ID, 'weight')
compute_btn = browser.find_element(By.XPATH, '//*[@value="computeBMI"]')


# 1. teszteset
# form kitöltése, submit
height.send_keys('171')
weight.send_keys('45')
compute_btn.click()

# Az eredményeket tartalmazó elementet változóba mentjük
result_bmi = browser.find_element(By.XPATH, '//span[@id="output"]/..').text
result_verdict = browser.find_element(By.XPATH, '//span[@id="comment"]/..').text

# A visszakapott eredményeket összehasonlítjuk az elvárt értékekkel
assert result_bmi == 'Your BMI is: 15'
assert result_verdict == 'This means you are: Underweight'

# inputmezők törlése
height.clear()
weight.clear()


# 2. teszteset
height.send_keys('185')
weight.send_keys('65')
compute_btn.click()

result_bmi = browser.find_element(By.XPATH, '//span[@id="output"]/..').text
result_verdict = browser.find_element(By.XPATH, '//span[@id="comment"]/..').text

assert result_bmi == 'Your BMI is: 19'
assert result_verdict == 'This means you are: Normal'
