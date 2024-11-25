from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self._driver = driver

    # добавление товаров в корзину
    # добавляем рюкзак
    def adding_to_cart_backpack(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

    # добавляем футболку
    def adding_to_cart_tshirt(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # добавляем комбинезон
    def adding_to_cart_onesie(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    # переход в корзину
    # через переменную, чтобы влезть в 79 символов
    def button_shopping_cart(self):
        cart_link = 'a.shopping_cart_link[data-test="shopping-cart-link"]'
        self._driver.find_element(By.CSS_SELECTOR, cart_link).click()
