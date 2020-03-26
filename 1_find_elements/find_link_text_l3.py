import math
import time
from selenium import webdriver
from config import chrome_path

browser = webdriver.Chrome(chrome_path)
orig_link = 'https://www.degreesymbol.net/'
browser.get(orig_link)
# link = browser.find_element_by_link_text("» Degree symbol examples")
# link.click()
link = browser.find_element_by_partial_link_text("examples")
link.click()

browser.get('http://suninjuly.github.io/find_link_text')

second_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
link_2 = browser.find_element_by_link_text(second_link)
link_2.click()
input1 = browser.find_element_by_tag_name("input.form-control")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(7)
browser.quit()
