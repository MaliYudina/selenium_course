from config import chrome_path
from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'upload_file.txt')


def upload_file():
    try:
        link = 'http://suninjuly.github.io/file_input.html'
        browser = webdriver.Chrome(chrome_path)
        browser.maximize_window()
        browser.get(link)
        f_name = browser.find_element_by_name("firstname")
        f_name.send_keys("Ivan")
        l_name = browser.find_element_by_name("lastname")
        l_name.send_keys("Petrov")
        e_mail = browser.find_element_by_name("email")
        e_mail.send_keys("ex@mail.ru")
        upload_button = browser.find_element_by_id("file")
        upload_button.send_keys(file_path)
        submit_button = browser.find_element_by_class_name("btn-primary")
        submit_button.click()
    finally:
        time.sleep(15)
        browser.quit()


upload_file()
