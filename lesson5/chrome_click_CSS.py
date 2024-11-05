from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(
    service=Service(
        'C:\\Users\\Настяя\\Desktop\\Homework\\lesson5\\chromedriver.exe'),
    options=chrome_options
)
driver.get("http://uitestingplayground.com/classattr")
sleep(1)
blue_button = driver.find_element(
    By.CSS_SELECTOR, "button.btn.class3.btn-primary.btn-test")
blue_button.click()
sleep(5)
driver.quit()
