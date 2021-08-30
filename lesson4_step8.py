from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Находим кнопку Book и скроллим вниз
    button = browser.find_element(By.ID, "book")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", button)

    # Дождаемся, когда цена дома уменьшится до $100 (ожидание 12 секунд)
    text1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем кнопку Book 
    button.click()

    # Находим значение х на странице и вычисляем функцию
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    # Вводим ответ в поле
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)    

    # Нажимаем кнопку Submit.
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
