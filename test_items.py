import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_find_button_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(5)
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        flag_but = True
    except NoSuchElementException:
        flag_but = False
    assert flag_but, 'Такой кнопки нет ;('
