link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_different_interface_language(browser):
    browser.get(link)
    browser.find_element_by_css_selector('[class="add-to-basket"]')