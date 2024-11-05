from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(1)
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
sleep(1)
input_field.clear()
sleep(1)
input_field.send_keys("999")
sleep(5)
driver.quit()
