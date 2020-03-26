from config import chrome_path
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def select_value():
    try:
        link = 'http://suninjuly.github.io/selects1.html'
        browser = webdriver.Chrome(chrome_path)
        browser.get(link)
        num_1 = browser.find_element_by_id("num1")
        num_1 = num_1.text
        num_2 = browser.find_element_by_id("num2")
        num_2 = num_2.text
        num_sum = int(num_1) + int(num_2)
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(str(num_sum))
        button = browser.find_element_by_class_name("btn-default")
        button.click()
    finally:
        time.sleep(15)
        browser.quit()


select_value()
