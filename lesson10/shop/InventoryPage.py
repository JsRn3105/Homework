import allure
from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Страница товаров.
    Содержит методы для добавления товаров в корзину и перехода в корзину.
    """
    def __init__(self, driver):
        """
        Инициализация класса страницы товаров.
        """
        self._driver = driver

    # Добавляем рюкзак в корзину
    @allure.step("Добавить рюкзак в корзину")
    def adding_to_cart_backpack(self) -> None:
        """
        Добавляем рюкзак в корзину.
        """
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Добавляем футболку в корзину
    @allure.step("Добавить футболку в корзину")
    def adding_to_cart_tshirt(self) -> None:
        """
        Добавляем футболку в корзину.
        """
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Добавляем комбинезон в корзину
    @allure.step("Добавить комбинезон в корзину")
    def adding_to_cart_onesie(self) -> None:
        """
        Добавляем комбинезон в корзину.
        """
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    @allure.step("Перейти в корзину, нажав на иконку корзины")
    def button_shopping_cart(self) -> None:
        """
        Переходим в корзину для оформления заказа.
        """
        cart_link = 'a.shopping_cart_link[data-test="shopping-cart-link"]'
        self._driver.find_element(By.CSS_SELECTOR, cart_link).click()
