from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
sleep(1)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
sleep(1)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
sleep(1)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(5)
driver.quit()
