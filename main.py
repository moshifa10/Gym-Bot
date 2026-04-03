from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import dotenv

dotenv.load_dotenv()

# ENV
GYM_URL = os.getenv(key="GYM_URL")
ACCOUNT_EMAIL = os.getenv(key="ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv(key="ACCOUNT_PASSWORD")

web = webdriver.ChromeOptions()
web.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
web.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=web)
driver.get(GYM_URL)


# Login Automatically
button = driver.find_element(By.ID, "login-button")
button.click()


# send keys

time.sleep(2)
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.XPATH, '//*[@id="password-input"]')
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
login = driver.find_element(By.ID, "submit-button")
login.click()
