import math
from config import chrome_path
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def get_html():
    try:
        link = 'http://suninjuly.github.io/get_attribute.html'
        browser = webdriver.Chrome(chrome_path)
        browser.get(link)
        # people_radio = browser.find_element_by_id("peopleRule")
        # people_checked = people_radio.get_attribute("checked")
        # print("value of people radio: ", people_checked)
        # assert people_checked is not None, "People radio is not selected by default"
        x_element = browser.find_element_by_id("treasure")
        x = x_element.get_attribute("valuex")
        y = calc(x)
        answer_field = browser.find_element_by_id("answer")
        answer_field.send_keys(str(y))
        option1 = browser.find_element_by_id("robotCheckbox")
        option1.click()
        option2 = browser.find_element_by_id("robotsRule")
        option2.click()
        button = browser.find_element_by_class_name("btn-default")
        button.click()
    finally:
        time.sleep(30)
        browser.quit()


get_html()

