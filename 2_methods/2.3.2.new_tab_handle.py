from config import chrome_path
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def select_value():
    try:
        link = 'http://suninjuly.github.io/redirect_accept.html'
        browser = webdriver.Chrome(chrome_path)
        browser.maximize_window()
        browser.get(link)

        button = browser.find_element_by_class_name("btn-primary")
        button.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x_element = browser.find_element_by_id("input_value")
        x = x_element.text
        y = calc(x)

        answer_field = browser.find_element_by_id("answer")
        answer_field.send_keys(str(y))

        button = browser.find_element_by_class_name("btn-primary")
        button.click()
        alert = browser.switch_to.alert
        alert_text = alert.text

        text = alert_text.split(': ')[-1]
        print(text)
    finally:
        time.sleep(15)
        browser.quit()


select_value()
