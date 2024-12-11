import allure
from selenium.webdriver.common.by import By


class LoginPage:
    """
    Страница входа в систему.
    Содержит методы для ввода логина, пароля и кнопки входа.
    """
    def __init__(self, driver):
        """
        Конструктор для инициализации страницы
        входа в браузере через WebDriver.
        """
        # Запуск браузера, открытие сайта
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        # Ожидание в 4 секунды для прогрузки страницы
        self._driver.implicitly_wait(4)
        # Разворачивание окна во весь экран
        self._driver.maximize_window()

    # Вводим логин пользователя
    @allure.step("Ввести логин пользователя")
    def login_input(self, username: str) -> None:
        """
        Вводим логин в поле формы.
        """
        self._driver.find_element(By.ID, "user-name").send_keys(username)

    # Вводим пароль пользователя
    @allure.step("Ввести пароль пользователя")
    def password_input(self, password: str) -> None:
        """
        Вводим пароль в поле формы.
        """
        self._driver.find_element(By.ID, "password").send_keys(password)

    # Нажимаем кнопку Login для авторизации с введёнными данными
    @allure.step("Нажать кнопку 'Login'")
    def button_login(self) -> None:
        """
        Нажимаем кнопку входа для авторизации.
        """
        self._driver.find_element(By.ID, "login-button").click()
