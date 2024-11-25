from selenium import webdriver
from form.MainForm import MainForm
from form.FormCheck import FormCheck


# инициируем открытие браузера, переходим на сайт
def test_form_submission():
    browser = webdriver.Chrome()
    main_form = MainForm(browser)
    # вводим имя, фамилию, адрес, почту, номер телефона
    # город, страну, должность и название компании
    # поле индекса оставляем пустым
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
    main_form.submit_button()

    form_check = FormCheck(browser)
    # Для zip-code ожидаем alert-danger
    expected_classes = {
        "zip-code": "alert-danger",
    }
    fields = ["first-name", "last-name", "address", "e-mail", "phone",
              "zip-code", "city", "country", "job-position", "company"]

    for field_id in fields:
        # Для поля zip-code ожидаем класс alert-danger,
        # для остальных alert-success
        expected_class = expected_classes.get(field_id, "alert-success")
        # Получаем фактический класс поля и сверяем с ожидааемым
    field_class = form_check.get_field_class(field_id)
    assert expected_class in field_class

    browser.quit()
