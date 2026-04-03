from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

web = webdriver.ChromeOptions()
web.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
web.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=web)
driver.get(os.getenv(key="GYM_URL"))
