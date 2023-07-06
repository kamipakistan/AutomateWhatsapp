import time  # Importing the time module for delays and time-related functions
from selenium import webdriver  # Importing the Selenium WebDriver module
from selenium.webdriver.chrome.options import Options  # Importing options for configuring Chrome WebDriver
from selenium.webdriver.common.by import By  # Importing By class for locating elements
from selenium.webdriver.common.keys import Keys  # Importing Keys class for keyboard keys
from selenium.webdriver.support import \
    expected_conditions  # Importing expected_conditions for waiting until certain conditions are met
from selenium.webdriver.support.ui import \
    WebDriverWait  # Importing WebDriverWait for waiting until certain conditions are met
from webdriver_manager.chrome import \
    ChromeDriverManager  # Importing ChromeDriverManager for automatically downloading and managing the Chrome WebDriver
from selenium.webdriver.chrome.service import Service  # Importing Service class for starting the ChromeDriver service


def send_whatsapp_message(message, phone_number):
    BASE_URL = "https://web.whatsapp.com/"  # Base URL for WhatsApp Web
    CHAT_URL = f"https://web.whatsapp.com/send?phone={phone_number}&text&type=phone_number&app_absent=1"  # URL for opening a chat with a specific phone number

    # Instructions for finding the Chrome user profile folder:
    # Visit: https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/

    # Path to your Chrome user profile directory
    CHROME_USER_PROFILE_PATH = "/home/kamipakistan/.config/google-chrome/Default"

    chrome_options = Options()  # Creating an instance of ChromeOptions class for configuring Chrome WebDriver options
    chrome_options.add_argument("start-maximized")  # Maximizing the browser window
    chrome_options.add_argument(
        f"--user-data-dir={CHROME_USER_PROFILE_PATH}")  # Setting the user profile directory for Chrome

    chrome_service = Service(ChromeDriverManager().install())  # Creating an instance of Service class for ChromeDriver

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)  # Creating a Chrome WebDriver instance

    browser.get(BASE_URL)  # Opening the base URL
    browser.maximize_window()  # Maximizing the browser window

    browser.get(CHAT_URL)  # Opening the chat URL with the provided phone number
    time.sleep(6)  # Pausing for 6 seconds to allow the page to load

    input_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'  # XPath for the input box element
    input_box = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, input_box_xpath))
        # Waiting until the input box element is present
    )
    input_box.send_keys(message)  # Entering the message into the input box
    input_box.send_keys(Keys.ENTER)  # Sending the message by pressing Enter key

    time.sleep(15)  # Pausing for 15 seconds


if __name__ == "__main__":
    phone_number = "+923435319075"  # The phone number to send the message to
    message = 'Hi There. This is a test message from Kamran Khan'  # The message to be sent
    send_whatsapp_message(message, phone_number)  # Calling the send_whatsapp_message function to send the message
