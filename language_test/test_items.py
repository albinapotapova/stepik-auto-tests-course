link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_interface_language(browser):
    try:
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector('[class="add-to-basket"]')
        return True
    except:
        return False    
    assert test_different_interface_language(
        browser) == True, "Корзина не найдена"
