from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath("/html/body/div/form/div/div/div[1]/h2/img")
x = x_element.get_attribute("valuex")
y = calc(x)

input1 = browser.find_element_by_xpath("/html/body/div/form/div/div/input")
input1.send_keys(y)

option1 = browser.find_element_by_xpath("/html/body/div/form/div/div/div[2]/input[1]")
option1.click()

option2 = browser.find_element_by_xpath("/html/body/div/form/div/div/div[2]/input[3]")
option2.click()

option3 = browser.find_element_by_css_selector("body > div > form > div > div > button")
option3.click()

print(y)
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()

