import math
from config import chrome_path
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def get_html():
    try:
        link = 'http://suninjuly.github.io/math.html'
        browser = webdriver.Chrome(chrome_path)
        browser.get(link)
        x_element = browser.find_element_by_id("input_value")
        x = x_element.text
        y = calc(x)
        answer_field = browser.find_element_by_id("answer")
        answer_field.send_keys(str(y))
        option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
        option1.click()
        option2 = browser.find_element_by_css_selector("[for='robotsRule']")
        option2.click()
        button = browser.find_element_by_class_name("btn-default")
        button.click()
    finally:
        time.sleep(30)
        browser.quit()


get_html()

