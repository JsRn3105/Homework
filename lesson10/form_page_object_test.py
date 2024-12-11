import allure
from selenium import webdriver
from form.MainForm import MainForm
from form.FormCheck import FormCheck


@allure.suite("Заполнение и отправка формы")
@allure.title("Тест отправки формы")
@allure.description(
    "Этот тест проверяет валидность отправки формы с несколькими полями, " +
    "включая проверку на заполненность каждого поля после отправки.")
@allure.feature("Форма отправки")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission():
    """
    Тест для проверки отправки формы и валидации данных.

    1. Заполняются все поля формы (в данном тесте кроме zip-code).
    2. После отправки формы проверяются присвоенные классы элементов,
    для незаполненных (zip-code) 'alert-danger'
    для заполненных полей (все остальные) ожидается 'alert-success'.
    """
    # Запускаем инициализацию браузера, переходим на сайт формы
    with allure.step("Запустить браузер и перейти на страницу формы"):
        browser = webdriver.Chrome()

    with allure.step("Создать объект формы и начать заполнение данных"):
        main_form = MainForm(browser)

    # Для этого теста заполняем все поля формы, кроме zip-code
    with allure.step("Ввести данные в форму"):
        main_form.input_first_name("Иван")
        main_form.input_last_name("Петров")
        main_form.input_address("Ленина, 55-3")
        main_form.input_email("test@skypro.com")
        main_form.input_phone("+7985899998787")
        main_form.input_zip_code("")
        main_form.input_city("Москва")
        main_form.input_country("Россия")
        main_form.input_job_position("QA")
        main_form.input_company("SkyPro")

    # Отправляем форму
    with allure.step("Отправить форму"):
        main_form.submit_button()

    # Проверяем  результаты
    form_check = FormCheck(browser)

    # Для zip-code ожидаем alert-danger
    expected_classes = {
        "zip-code": "alert-danger",
    }
    fields = ["first-name", "last-name", "address", "e-mail", "phone",
              "zip-code", "city", "country", "job-position", "company"]

    # Проверка классов для всех полей
    with allure.step("Проверить классы для всех полей формы"):
        for field_id in fields:
            # Для поля zip-code ожидаем класс alert-danger
            # для остальных alert-success
            expected_class = expected_classes.get(field_id, "alert-success")
            # Получаем фактический класс поля и сверяем с ожидаемым
        field_class = form_check.get_field_class(field_id)

        with allure.step(f"Проверить класс для поля {field_id}"):
            assert expected_class in field_class

    # Закрываем браузер
    with allure.step("Закрыть браузер"):
        browser.quit()
