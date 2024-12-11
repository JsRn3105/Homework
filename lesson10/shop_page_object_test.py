import allure
from selenium import webdriver
from shop.LoginPage import LoginPage
from shop.InventoryPage import InventoryPage
from shop.CartCheckout import CartCheckout


@allure.suite("Оформления заказа в корзине")
@allure.title("Тест оформления заказа в корзине")
@allure.description("Этот тест проверяет добавление товаров в корзину, " +
                    "оформление заказа с вводом данных " +
                    "и сверку итоговой суммы товаров в корзине с ожидаемой.")
@allure.feature("Корзина и оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart_checkout():
    """
    Тест для проверки оформления заказа в корзине с добавлением товаров
    и сверки итоговой суммы заказа с ожидаемой.

    1. Входим в существующую учётную запись с корректными учетными данными.
    2. Добавляем несколько товаров в корзину.
    3. Переходим к оформлению заказа
     и вводим валидные данные в обязательные для заполнения поля.
    4. Сверяем итоговую цену с ожидаемой.
    """
    # Запускаем инициализацию браузера и переходим на страницу входа
    with allure.step("Запуск браузера и переход на страницу входа"):
        browser = webdriver.Chrome()
        login_page = LoginPage(browser)

    # Вводим логин и пароль
    with allure.step("Ввести логин и пароль для авторизации"):
        login_page.login_input("standard_user")
        login_page.password_input("secret_sauce")

    # Нажимаем кнопку Login для авторизации
    with allure.step("Нажать кнопку 'Login' для авторизации"):
        login_page.button_login()

    # Добавляем товары в корзину
    with allure.step("Добавить товары в корзину: " +
                     "'Backpack', 'Bolt T-Shirt', 'Onesie'"):
        inventory_page = InventoryPage(browser)
        inventory_page.adding_to_cart_backpack()
        inventory_page.adding_to_cart_tshirt()
        inventory_page.adding_to_cart_onesie()

    # Переходим в корзину
    with allure.step("Перейти в корзину, кликнув на иконку корзины"):
        inventory_page.button_shopping_cart()

    # Переходим к форме ввода личных данных для заказа
    with allure.step("Нажать кнопку 'Checkout'"):
        cart_checkout = CartCheckout(browser)
        cart_checkout.checkout_button()

    # Заполняем поля Имя, Фамилия и Почтовый индекс
    with allure.step("Заполнить валидными данными поля 'First Name', " +
                     "'Last Name' и 'Zip/Postal Code'"):
        cart_checkout.first_name_input("Анастасия")
        cart_checkout.last_name_input("Макарова")
        cart_checkout.index_input("222222")

    # Нажимаем кнопку Продолжить
    with allure.step("Нажать кнопку 'Continue'"):
        cart_checkout.continue_button()

    # Получаем итоговую цену и вносим в переменную
    with allure.step("Получить итоговую сумму заказа"):
        total_price = cart_checkout.total_price()

    # Закрываем браузер
    with allure.step("Закрыть браузер"):
        browser.quit()

    # Сверяем ожидаемый результат с фактическим
    with allure.step("Сверить итоговую сумму с ожидаемой"):
        assert total_price == "Total: $58.29"
