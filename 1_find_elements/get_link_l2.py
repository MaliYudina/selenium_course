from selenium import webdriver
from selenium.webdriver.common.by import By
from config import chrome_path


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome(chrome_path)
browser.get(link)
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

# 22.282386075762314

# закрываем браузер после всех манипуляций


# закрываем браузер после всех манипуляций
# browser.quit()
