import allure
from selenium import webdriver
from calc.MainCalc import MainCalc
from calc.ResultCalc import ResultCalc


@allure.suite("Калькулятор с регулируемой задержкой вычисления результата")
@allure.title("Тест калькулятора с задержкой")
@allure.description(
    "Направлен на проверку корректности работы калькулятора: " +
    "выполнение простых операций, отображение результата " +
    "с задержкой и проверку результата.")
@allure.feature("Основной функционал калькулятора")
@allure.severity(allure.severity_level.NORMAL)
def test_delay_calculator():
    """
    Тест для проверки работы калькулятора с задержкой.

    1. Очистить поле ввода.
    2. Установить задержку в 45 секунд.
    3. Выполнить арифметическое действие (7 + 8).
    4. Сверить полученный результат с ожидаемым значением.
    """

    # Запускаем инициализацию браузера, переходим на сайт калькулятора
    with allure.step("Запустить браузер и перейти на сайт калькулятора"):
        browser = webdriver.Chrome()

    with allure.step("Создать объекта калькулятора"):
        main_calc = MainCalc(browser)

    # Очищаем поле ввода и ставим задержку в 45 секунд
    with allure.step("Очистить поле ввода задержки " +
                     "и проставить задержку в 45 секунд"):
        main_calc.clear_input_field()
        main_calc.delay_time_input("45")

    # Набираем 7+8 и жмём = для вычисления результата
    with allure.step(
        "Нажать кнопки калькулятора 7 + 8 для набора слагаемых и действия, " +
         "нажать = для запуска вычислений"):
        main_calc.button_seven()
        main_calc.button_addition()
        main_calc.button_eight()
        main_calc.button_equal()

    # Получаем результат
    with allure.step("Получить результат вычислений"):
        result_calc = ResultCalc(browser)
        result = result_calc.get_result()

    # Сверка ожидаемого результата с фактическим
    with allure.step("Проверить результат вычислений с ожидаемым"):
        assert result == "15"

    # Закрываем браузер
    with allure.step("Закрыть браузер"):
        browser.quit()
