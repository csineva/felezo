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

def fill_form(height, weight, bmi, verdict):
    height = browser.find_element(By.ID, 'height')
    weight = browser.find_element(By.ID, 'weight')
    compute_btn = browser.find_element(By.XPATH, '//*[@value="computeBMI"]')

    height.send_keys(height)
    weight.send_keys(weight)
    compute_btn.click()

    result_bmi = browser.find_element(By.XPATH, '//span[@id="output"]/..').text
    result_verdict = browser.find_element(By.XPATH, '//span[@id="comment"]/..').text

    print(result_bmi)
    print(result_verdict)
    assert result_bmi == bmi #'Your BMI is: 15'
    assert result_verdict == verdict #'This means you are: Underweight'


test_data = [
    {
        'height': 171,
        'weight': 45,
        'bmi': 'Your BMI is: 15',
        'verdict': 'This means you are: Underweight'
    },
    {
        'height': 171,
        'weight': 45,
        'bmi': 'Your BMI is: 19',
        'verdict': 'This means you are: Normal'
    }
]

for data in test_data:
    fill_form(data['height'], data['weight'], data['bmi'], data['verdict'])

# time.sleep(1)
