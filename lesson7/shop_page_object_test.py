from selenium import webdriver
from shop.LoginPage import LoginPage
from shop.InventoryPage import InventoryPage
from shop.CartCheckout import CartCheckout


# инициируем открытие браузера, переходим на сайт, логинимся
def test_shopping_cart_checkout():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)
    login_page.login_input("standard_user")
    login_page.password_input("secret_sauce")
    login_page.button_login()

    # добавляем товары в корзину
    inventory_page = InventoryPage(browser)
    inventory_page.adding_to_cart_backpack()
    inventory_page.adding_to_cart_tshirt()
    inventory_page.adding_to_cart_onesie()
    # переходим в корзину
    inventory_page.button_shopping_cart()

    # переходим к вводу имени, фамилии, индекса
    cart_checkout = CartCheckout(browser)
    cart_checkout.checkout_button()
    cart_checkout.first_name_input("Анастасия")
    cart_checkout.last_name_input("Макарова")
    cart_checkout.index_input("222222")
    cart_checkout.continue_button()

    # вносим в переменную итоговую сумму
    total_price = cart_checkout.total_price()

    browser.quit()

    # сверка ожидаемого результата с фактическим
    assert total_price == "Total: $58.29"
