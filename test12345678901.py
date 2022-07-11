from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return math.log(abs(12*math.sin(int(x))))
try:
    browser = webdriver.Chrome()  
    browser.get(link)
    x1 = browser.find_element_by_id("input_value")
    x2 = int(x1.text)
    x3 = str(calc(x2))
    print(x3)
    browser.execute_script("window.scrollBy(0, 100);")
    viewone = browser.find_element_by_id("answer")
    viewone.send_keys(x3)
    checbox = browser.find_element_by_id("robotCheckbox")
    checbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
