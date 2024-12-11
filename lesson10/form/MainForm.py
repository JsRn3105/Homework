import allure
from selenium.webdriver.common.by import By


class MainForm:
    """
    Класс для взаимодействия с основной формой на веб-странице.

    Этот класс предоставляет методы для ввода данных в различные поля формы
    и метод для отправки формы.
    """
    def __init__(self, driver):
        """
        Конструктор для инициализация страницы формы
        и открытие сайта в браузере через WebDriver.
        """
        # Запуск браузера, открытие сайта
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        # Ожидание в 4 секунды для прогрузки страницы
        self._driver.implicitly_wait(4)
        # Разворачивание окна во весь экран
        self._driver.maximize_window()

    # Вводим имя
    @allure.step("Ввести имя")
    def input_first_name(self, term: str) -> None:
        """
        Вводим имя в поле формы.
        """
        self._driver.find_element(By.NAME, "first-name").send_keys(term)

    # Вводим фамилию
    @allure.step("Ввести фамилию")
    def input_last_name(self, term: str) -> None:
        """
        Вводим фамилию в поле формы.
        """
        self._driver.find_element(By.NAME, "last-name").send_keys(term)

    # Вводим адрес
    @allure.step("Ввести адрес")
    def input_address(self, term: str) -> None:
        """
        Вводим адрес в поле формы.
        """
        self._driver.find_element(By.NAME, "address").send_keys(term)

    # Вводим e-mail
    @allure.step("Ввести e-mail")
    def input_email(self, term: str) -> None:
        """
        Вводим email в поле формы.
        """
        self._driver.find_element(By.NAME, "e-mail").send_keys(term)

    # Вводим номер телефона
    @allure.step("Ввести номер телефона")
    def input_phone(self, term: str) -> None:
        """
        Вводим номер телефона в поле формы.
        """
        self._driver.find_element(By.NAME, "phone").send_keys(term)

    # Вводим индекс - для этого теста поле оставляем пустым
    @allure.step("Ввести индекс")
    def input_zip_code(self, term: str) -> None:
        """
        Вводим индекс в поле формы.
        """
        self._driver.find_element(By.NAME, "zip-code").send_keys(term)

    # Вводим город
    @allure.step("Ввести город")
    def input_city(self, term: str) -> None:
        """
        Вводим город в поле формы.
        """
        self._driver.find_element(By.NAME, "city").send_keys(term)

    # Вводим страну
    @allure.step("Ввести страну")
    def input_country(self, term: str) -> None:
        """
        Вводим страну в поле формы.
        """
        self._driver.find_element(By.NAME, "country").send_keys(term)

    # Вводим название должности
    @allure.step("Ввести должность")
    def input_job_position(self, term: str) -> None:
        """
        Вводим должность в поле формы.
        """
        self._driver.find_element(By.NAME, "job-position").send_keys(term)

    # Вводим название компании
    @allure.step("Ввести название компании")
    def input_company(self, term: str) -> None:
        """
        Вводим название компании в поле формы.
        """
        self._driver.find_element(By.NAME, "company").send_keys(term)

    # Отправляем данные
    @allure.step("Нажать кнопку отправки формы")
    def submit_button(self) -> None:
        """
        Нажимаем кнопку отправки формы.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()
