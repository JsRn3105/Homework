import allure
from selenium.webdriver.common.by import By


class CartCheckout:
    """
    Страница оформления заказа в корзине.
    Содержит методы для ввода данных,
    оформления заказа и получения итоговой суммы.
    """
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        """
        self._driver = driver

    # Нажимаем кнопку 'Checkout', чтобы перейти к оформлению заказа
    @allure.step("Нажать кнопку 'Checkout' для начала оформления заказа")
    def checkout_button(self) -> None:
        """
        Нажимаем кнопку 'Checkout', чтобы перейти к оформлению заказа.
        """
        self._driver.find_element(By.ID, "checkout").click()

    # Вводим имя покупателя
    @allure.step("Ввести имя покупателя")
    def first_name_input(self, first_name: str) -> None:
        """
        Вводим имя покупателя.
        """
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)

    # Вводим фамилию покупателя
    @allure.step("Ввести фамилию покупателя")
    def last_name_input(self, last_name: str) -> None:
        """
        Вводим фамилию покупателя.
        """
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)

    # Вводим индекс покупателя
    @allure.step("Ввести индекс покупателя")
    def index_input(self, postal_code: str) -> None:
        """
        Вводим индекс покупателя.
        """
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    # Нажимаем кнопку 'Continue' для перехода к следующему шагу
    @allure.step("Нажать кнопку 'Continue' для продолжения оформления заказа")
    def continue_button(self) -> None:
        """
        Нажимаем кнопку 'Continue' для перехода к следующему шагу.
        """
        self._driver.find_element(By.ID, "continue").click()

    # Получаем итоговую сумму из элемента на странице
    # и вносим в переменную
    @allure.step("Получить итоговую сумму")
    def total_price(self) -> str:
        """
        Получаем итоговую сумму из элемента на странице.
        """
        total_price = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        return total_price
