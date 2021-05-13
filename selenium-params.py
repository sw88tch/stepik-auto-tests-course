import pytest, time, math
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

links = ['236895', '236896','236897', '236898', '236899', '236903', '236904', '236905']
final = []

@pytest.fixture(scope = "function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(final)

@pytest.mark.parametrize('url', links)
def test(browser, url):
    answer = math.log(int(time.time()))
    browser.get(f'https://stepik.org/lesson/{url}/step/1')
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea')))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_class_name('submit-submission').click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__feedback')))
    correct_checker = browser.find_element_by_class_name('smart-hints__feedback').text
    assert correct_checker == 'Correct!', f"Message -> {correct_checker}"