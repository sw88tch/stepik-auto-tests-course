import unittest
import time
from selenium import webdriver

class TestSystem(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
       # element_registration = browser.find_element_by_css_selector('h1').text
        name = browser.find_element_by_css_selector('.first_block>.first_class>.first')
        name.send_keys('Kirill')
        lastname = browser.find_element_by_css_selector('.first_block>.second_class>.second')
        lastname.send_keys('Kalinin')
        mail = browser.find_element_by_css_selector('.first_block>.third_class>.third')
        mail.send_keys('pochta@email.com')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        congratulation = browser.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!',
                         "button_click_error")

        time.sleep(5)
        browser.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser2 = webdriver.Chrome()
        browser2.get(link)
        # element_registration = browser2.find_element_by_css_selector('h1').text
        name = browser2.find_element_by_css_selector('.first_block>.first_class>.first')
        name.send_keys('Kirill')
        lastname = browser2.find_element_by_css_selector('.first_block>.second_class>.second')
        lastname.send_keys('Kalinin')
        mail = browser2.find_element_by_css_selector('.first_block>.third_class>.third')
        mail.send_keys('pochta@email.com')
        button = browser2.find_element_by_css_selector("button.btn")
        button.click()
        congratulation = browser2.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!',
                             "button_click_error")

        time.sleep(5)
        browser2.quit()

if __name__ == "__main__":
    unittest.main()