from selenium.webdriver.common.by import By


class LoginPage:
    # запуск браузера, открытие сайта и разворачивание окна во весь экран
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    # ввод логина
    def login_input(self, term):
        self._driver.find_element(By.ID, "user-name").send_keys(term)

    # ввод пароля
    def password_input(self, term):
        self._driver.find_element(By.ID, "password").send_keys(term)

    # нажать кнопку Login
    def button_login(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[type='submit']").click()
