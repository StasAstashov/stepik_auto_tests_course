from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
findbox = driver.find_element_by_xpath('//ytd-searchbox/form/div/div[1]/input')
findbox.send_keys('ss')
findbutton = driver.find_element_by_xpath('//ytd-searchbox/button/yt-icon')
findbutton.click()