from config import chrome_path
from selenium import webdriver
from selenium.common.exceptions import *
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(chrome_path)
    browser.get(link)

    name = browser.find_element_by_class_name("form-control.first")
    name.send_keys("Ivan")

    l_name = browser.find_element_by_class_name("form-control.second")
    l_name.send_keys("Ivanov")

    email = browser.find_element_by_class_name("form-control.third")
    email.send_keys("mail@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(6)
    button.click()
    time.sleep(4)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
