from selenium.webdriver.common.by import By


class CartCheckout:
    def __init__(self, driver):
        self._driver = driver

    # кнопка checkout
    def checkout_button(self):
        self._driver.find_element(By.ID, "checkout").click()

    # ввод имени
    def first_name_input(self, term):
        self._driver.find_element(By.ID, "first-name").send_keys(term)

    # ввод фамилии
    def last_name_input(self, term):
        self._driver.find_element(By.ID, "last-name").send_keys(term)

    # ввод индекса
    def index_input(self, term):
        self._driver.find_element(By.ID, "postal-code").send_keys(term)

    # кнопка continue
    def continue_button(self):
        self._driver.find_element(By.ID, "continue").click()

    # вносим в переменную итоговую сумму
    def total_price(self):
        total_price = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        return total_price
