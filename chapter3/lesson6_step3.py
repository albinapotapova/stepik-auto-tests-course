import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('web', ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, web):
    browser.get(web)
    answer = math.log(int(time.time()))
    text1 = browser.find_element_by_css_selector(
        '[placeholder="Type your answer here..."]')
    text1.send_keys(str(answer))
    button = browser.find_element_by_css_selector(
        '[class = "submit-submission"]')
    button.click()
    feedback = browser.find_element_by_css_selector(
        '[class="smart-hints__hint"]')
    feed = feedback.text
    assert feed == 'Correct!', "Correct!"

