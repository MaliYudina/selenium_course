from selenium import webdriver
from selenium.webdriver.common.by import By
from config import chrome_path

browser = webdriver.Chrome(chrome_path)
orig_link = 'https://www.maxidom.ru/catalog/izmeritelnyjj-instrument/'
browser.get(orig_link)

add_button = browser.find_elements_by_css_selector(".button-cart")
for b in add_button:
    b.click()


# browser.get('https://www.maxidom.ru/catalog/niveliry-lazernye/1000841100/')
# add_button = browser.find_element_by_css_selector(".button-cart")
# add_button.click()

browser.get("https://www.maxidom.ru/personal/cart/")
goods = browser.find_elements_by_css_selector(".item-cart")
print(len(goods))
assert len(goods) == 1

