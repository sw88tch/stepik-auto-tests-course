from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
input1.send_keys("Kirill")

input2 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
input2.send_keys("Kalinin")

input3 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)")
input3.send_keys("mail@ya.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(file_path)

button = browser.find_element_by_css_selector("body > div > form > button")
button.click()

time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()