from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
sleep(1)
add_button = driver.find_element(
    By.CSS_SELECTOR, "button[onclick='addElement()']")
for _ in range(5):
    add_button.click()
delete_buttons = driver.find_elements(
    By.CSS_SELECTOR, "button.added-manually")
print(len(delete_buttons))
sleep(5)
driver.quit()
