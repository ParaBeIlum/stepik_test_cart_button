import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').is_displayed(),\
        'Button not found'
