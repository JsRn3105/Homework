from selenium import webdriver
from calc.MainCalc import MainCalc
from calc.ResultCalc import ResultCalc


# инициируем запуск браузера, переходим на сайт
def test_delay_calculator():
    browser = webdriver.Chrome()
    main_calc = MainCalc(browser)
    # очищаем поле ввода и ставим задержку 45 секунд
    main_calc.clear_input_field()
    main_calc.delay_time_input("45")
    # набираем 7+8и жмём = для вычисления результата
    main_calc.button_seven()
    main_calc.button_addition()
    main_calc.button_eight()
    main_calc.button_equal()

    # получение результата
    result_calc = ResultCalc(browser)
    result = result_calc.get_result()

    # сверка ожидаемого результата с фактическим
    assert result == "15"

    browser.quit()
