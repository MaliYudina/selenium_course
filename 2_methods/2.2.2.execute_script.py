from config import chrome_path
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def select_value():
    try:
        link = 'http://suninjuly.github.io/execute_script.html'
        browser = webdriver.Chrome(chrome_path)
        browser.maximize_window()
        browser.get(link)
        x_element = browser.find_element_by_id("input_value")
        x = x_element.text
        y = calc(x)
        answer_field = browser.find_element_by_id("answer")
        answer_field.send_keys(str(y))
        option1 = browser.find_element_by_id("robotCheckbox")
        option1.click()
        option2 = browser.find_element_by_id("robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
        option2.click()
        button = browser.find_element_by_class_name("btn-primary")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
    finally:
        time.sleep(15)
        browser.quit()


select_value()
