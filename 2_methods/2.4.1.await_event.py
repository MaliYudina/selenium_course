from config import chrome_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(chrome_path)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element_by_id("book")

button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(str(y))

button_solve = browser.find_element_by_id("solve")
button_solve.click()
alert = browser.switch_to.alert
alert_text = alert.text

text = alert_text.split(': ')[-1]
print(text)
