from selenium.webdriver.common.by import By


class MainCalc:
    # запуск браузера, открытие сайта и разворачивание окна во весь экран
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/" +
                         "slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    # очистка поля ввода
    def clear_input_field(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    # установка времени задержки
    def delay_time_input(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)

    # кнопки с числами и знаками действий на калькуляторе
    # упрощенный вариант: только нужные нам числа и знаки
    def button_seven(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()

    def button_eight(self):
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()

    def button_addition(self):
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()

    def button_equal(self):
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
