import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultCalc:
    """
    Класс для получения и проверки результата
    вычислений на странице калькулятора.

    Этот класс предоставляет методы для ожидания
    появления результата вычислений и его получения.
    """
    def __init__(self, driver):
        """
        Конструктор для инициализации класса.
        """
        self._driver = driver

    # Ожидаем появления результата вычислений
    @allure.step("Дождаться появления результата на экране")
    def get_result(self) -> str:
        """
        Метод для получения результата вычислений с экрана калькулятора.
        Этот метод ждет появления текста '15' в поле с результатом,
        затем извлекает и возвращает текст результата.
        """

        # Ожидаем, что результат на экране калькулятора будет равен '15'
        with allure.step("Дождаться, что результат '15' появится на экране"):
            WebDriverWait(self._driver, 45).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".screen"), "15"
                )
            )

        # Извлекаем и возвращаем текст результата
        with allure.step("Получить результат вычислений с экрана"):
            result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text

        return result
