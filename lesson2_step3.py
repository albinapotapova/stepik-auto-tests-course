from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим числа и считаем их сумму
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    
    z = int(x) + int(y)
    
    # Ищем правильный ответ в выпадающем списке
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % z)

    # Нажимаем кнопку Submit.
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()