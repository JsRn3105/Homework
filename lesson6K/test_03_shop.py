import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


def test_shopping_cart_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR,
                        'a.shopping_cart_link[data-test="shopping-cart-link"]'
                        ).click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Анастасия")
    driver.find_element(By.ID, "last-name").send_keys("Макарова")
    driver.find_element(By.ID, "postal-code").send_keys("222222")
    driver.find_element(By.ID, "continue").click()
    total_price = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label").text
    driver.quit()
    assert total_price == "Total: $58.29"
