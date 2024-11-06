from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(
    service=Service(
        'C:\\Users\\Настяя\\Desktop\\Homework\\lesson6\\chromedriver.exe'),
    options=chrome_options
)
driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()
txt = driver.find_element(By.ID, "updatingButton").text
print(txt)
driver.quit()
