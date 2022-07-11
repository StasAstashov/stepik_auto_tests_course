from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your first name']")
    input1.send_keys("Пушкин")
    input2 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your last name']")
    input2.send_keys("Калатушкин")
    input3 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your email']")
    input3.send_keys("pushkin@kalatushkin.com")
    input4 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your phone:']")
    input4.send_keys("89999999999")
    input5 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your address:']")
    input5.send_keys("Улица Пушкина, дом калатушкина")
 # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//div//button[@type = 'submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print('okey')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
