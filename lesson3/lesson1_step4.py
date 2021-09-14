from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение х на странице и вычисляем функцию
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    # Вводим ответ в поле
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    # Ставим галочку в чекбоксе
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    # Выбраем radiobutton "Robots rule!"
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    # Нажимаем кнопку Submit.
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()