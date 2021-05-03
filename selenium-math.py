from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath("/html/body/div/form/div[1]/label/span[2]")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
input1.send_keys(y)

option1 = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
option1.click()

option2 = browser.find_element_by_xpath("/html/body/div/form/div[4]/input")
option2.click()

option3 = browser.find_element_by_css_selector("body > div > form > button")
option3.click()

print(y)
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()

