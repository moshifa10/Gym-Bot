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
        next_day = today + datetime.timedelta(days=i)
        if next_day.strftime("%A").lower() == "tuesday":
            tuesday = next_day
else: tuesday = today # 2026-04-04


# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0

# Find the class 
driver.implicitly_wait(4)
# class_find = driver.find_element(By.ID, f"class-time-spin-{tuesday}-1800")
book_button =driver.find_element(By.ID, f"book-button-spin-{tuesday}-1800")
name_of_the_class = driver.find_element(By.CSS_SELECTOR, f"h3#class-name-spin-{tuesday}-1800").text
# print(name_of_the_class)
if book_button.text.lower() == "waitlisted":
    waitlist_count +=1
    print(f"✓ Already on waitlist: {name_of_the_class} on {tuesday.strftime("%a")}, {tuesday.strftime("%B")} {tuesday.strftime("%m")}")
elif book_button.text.lower() == "booked":
    already_booked_count+=1
    print(f"✓ Already booked: {name_of_the_class} on {tuesday.strftime("%a")}, {tuesday.strftime("%B")} {tuesday.strftime("%m")}")
else:
    book_button.click()
    booked_count+=1
    print(f"✓ Booked: {name_of_the_class} on {tuesday.strftime("%a")}, {tuesday.strftime("%B")} {tuesday.strftime("%m")}")

# book-button-spin-2026-04-07-1800
# print(f"book-button-spin-{tuesday}-1800")


# Print summary
print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")