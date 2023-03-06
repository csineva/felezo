from datetime import datetime, date, time, timezone
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

URL = "https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/hogwards.html"
browser.get(URL)

# változókba mentjük az input elemeket
passenger = browser.find_element(By.ID, 'passenger')
departure_date = browser.find_element(By.ID, 'departure-date')
departure_time = browser.find_element(By.ID, 'departure-time')
issue_ticket = browser.find_element(By.ID, 'issue-ticket')

# tesztadatok
p_name = 'benedek istván'
select_date = date(2023, 6, 15)
# formázás
input_date_format = datetime.strftime(select_date, "%m/%d/%Y")

# kitöltjük majd elküldjük a formot
passenger.send_keys(p_name)
departure_date.send_keys(input_date_format)
departure_time.send_keys('03:30PM')
issue_ticket.click()

# kijelöljük az ellenőrizni kívánt elemeket
passenger_name = browser.find_element(By.ID, 'passenger-name').text
departure_date_text = browser.find_element(By.ID, 'departure-date-text').text
side_departure_date = browser.find_element(By.ID, 'side-detparture-date').text
departure_time_text = browser.find_element(By.ID, 'departure-time-text').text
side_departure_time = browser.find_element(By.ID, 'side-departure-time').text

check_date_format = datetime.strftime(select_date, "%Y-%m-%d")

# végrehajtjuk az ellenőrzést
assert passenger_name == p_name.upper()
assert departure_date_text == check_date_format
assert side_departure_date == check_date_format
assert departure_time_text == '03:30PM'
assert side_departure_time == '03:30PM'
