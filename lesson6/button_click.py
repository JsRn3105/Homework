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
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.ID, "ajaxButton").click()
driver.implicitly_wait(16)
content = driver.find_element(By.ID, "content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)
driver.quit()
