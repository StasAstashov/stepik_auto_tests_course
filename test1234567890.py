from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "https://SunInJuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()  
    browser.get(link)
    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
