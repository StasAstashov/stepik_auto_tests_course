from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input12 = browser.find_element_by_id('answer')
    input12.send_keys(y)
    checkbox1 = browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    checkbox12 = browser.find_element_by_id('robotsRule')
    checkbox12.click()
    button = browser.find_element_by_xpath("//div//button[@type = 'submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
