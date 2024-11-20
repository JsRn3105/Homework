from selenium.webdriver.common.by import By


class MainForm:
    # запуск браузера, открытие сайта и разворачивание окна во весь экран
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    # ввод имени
    def input_first_name(self, term):
        self._driver.find_element(By.NAME, "first-name").send_keys(term)

    # ввод фамилии
    def input_last_name(self, term):
        self._driver.find_element(By.NAME, "last-name").send_keys(term)

    # ввод адреса
    def input_address(self, term):
        self._driver.find_element(By.NAME, "address").send_keys(term)

    # ввод e-mail
    def input_email(self, term):
        self._driver.find_element(By.NAME, "e-mail").send_keys(term)

    # ввод номера телефона
    def input_phone(self, term):
        self._driver.find_element(By.NAME, "phone").send_keys(term)

    # ввод индекса
    def input_zip_code(self, term):
        self._driver.find_element(By.NAME, "zip-code").send_keys(term)

    # ввод города
    def input_city(self, term):
        self._driver.find_element(By.NAME, "city").send_keys(term)

    # ввод страны
    def input_country(self, term):
        self._driver.find_element(By.NAME, "country").send_keys(term)

    # ввод названия должности
    def input_job_position(self, term):
        self._driver.find_element(By.NAME, "job-position").send_keys(term)

    # ввод названия компании
    def input_company(self, term):
        self._driver.find_element(By.NAME, "company").send_keys(term)

    # кнопка для отправки данных
    def submit_button(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()
