import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "https://web.whatsapp.com/"
CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

# Path to your Chrome user profile directory
CHROME_USER_PROFILE_PATH = "/home/kamipakistan/.config/google-chrome/Default"

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument(f"--user-data-dir={CHROME_USER_PROFILE_PATH}")

chrome_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

browser.get(BASE_URL)
browser.maximize_window()

phone = "+923435319075"
message = 'Hi There. This is a test message from Kamran Khan'

browser.get(CHAT_URL.format(phone=phone))
time.sleep(6)

inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
input_box = WebDriverWait(browser, 60).until(
    expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
)
input_box.send_keys(message)
input_box.send_keys(Keys.ENTER)

time.sleep(15)
