from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath("/html/body/div/form/h2/span[2]")
x = int(x_element.text)
y_element = browser.find_element_by_xpath("/html/body/div/form/h2/span[4]")
y = int(y_element.text)
z = str(x + y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

option = browser.find_element_by_xpath("/html/body/div/form/button")
option.click()

time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()

