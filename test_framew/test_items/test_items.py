from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_basket_button(browser: webdriver.Chrome):
    #  browser - параметр, ": webdriver.Chrome" - это typehint
    browser.get(link)
    basket = browser.find_element_by_class_name("btn-add-to-basket")
    assert basket.is_displayed(), "Error! Button is not displayed"
