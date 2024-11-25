from selenium.webdriver.common.by import By


class FormCheck:
    def __init__(self, driver):
        self._driver = driver

    # получаем класс поля
    def get_field_class(self, field_id):
        # Возвращаем класс поля в зависимости от его заполненности
        return self._driver.find_element(
            By.ID, field_id).get_attribute("class")
