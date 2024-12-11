import allure
from selenium.webdriver.common.by import By


class MainCalc:
    """
    Класс для представления калькулятора.

    Этот класс предоставляет методы для взаимодействия с калькулятором
    на странице, такие как очистку поля ввода,
    ввод времени задержки и выполнение арифметических операций.
    """
    def __init__(self, driver):
        """
        Конструктор для инициализации страницы
        калькулятора в браузере через WebDriver.
        """
        # Запуск браузера, открытие сайта
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/" +
                         "slow-calculator.html")
        # Ожидание в 4 секунды для прогрузки страницы
        self._driver.implicitly_wait(4)
        # Разворачивание окна во весь экран
        self._driver.maximize_window()

    # Очистка поля ввода
    @allure.step("Очистить поле ввода")
    def clear_input_field(self) -> None:
        """
        Очищает поле ввода калькулятора.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    # Установка времени задержки
    @allure.step("Установить время задержки в поле ввода")
    def delay_time_input(self, term: str) -> None:
        """
        Вводит время задержки в поле ввода.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)

    # Кнопки с числами и знаками действий на калькуляторе
    # Упрощенный вариант: только нужные нам числа и знаки

    @allure.step("Нажать кнопку '7'")
    def button_seven(self) -> None:
        """
        Нажимает кнопку '7' на калькуляторе.
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()

    @allure.step("Нажать кнопку '8'")
    def button_eight(self) -> None:
        """
        Нажимает кнопку '8' на калькуляторе.
        """
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()

    @allure.step("Нажать кнопку '+'")
    def button_addition(self) -> None:
        """
        Нажимает кнопку '+' на калькуляторе.
        """
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()

    @allure.step("Нажать кнопку '=' для выполнения вычисления")
    def button_equal(self) -> None:
        """
        Нажимает кнопку '=' на калькуляторе для запуска вычисления результата.
        """
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
