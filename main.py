from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import dotenv
import datetime

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

driver.implicitly_wait(2)
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.XPATH, '//*[@id="password-input"]')
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
login = driver.find_element(By.ID, "submit-button")
login.click()


today = datetime.date.today()
day = today.strftime("%A").lower()

tuesday = None
if day != "tuesday":
    for i in range(1, 8):
        next_day = today + datetime.timedelta(days=8)
        if next_day.strftime("%A").lower() == "tuesday":
            tuesday = next_day
else: tuesday = today # 2026-04-04

# Find the class 
driver.implicitly_wait(2)
# class_find = driver.find_element(By.ID, f"class-time-spin-{tuesday}-1800")
book_button =driver.find_element(By.ID, f"book-button-spin-{tuesday}-1800")
book_button.click()
print(f"✓ Booked: Spin Class on {tuesday.strftime("%a")}, {tuesday.strftime("%B")} {tuesday.strftime("%m")}")




