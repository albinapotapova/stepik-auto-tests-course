from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем форму
    unput1 = browser.find_element_by_name('firstname')
    unput1.send_keys("Albina")

    unput2 = browser.find_element_by_name('lastname')
    unput2.send_keys("Potapova")

    unput3 = browser.find_element_by_name('email')
    unput3.send_keys("Albina@g.ru")
    
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'step8.txt')
    element = browser.find_element_by_name('file')
    element.send_keys(file_path)
    

    # Нажимаем кнопку Submit.
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()