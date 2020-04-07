from selenium import webdriver

from ..pages.home_page import HomePage


def test_text_search():
    # Открыть браузер
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Открыть диалог поиска
    text_search_dialog = home_page.get_text_search_dialog()
    text_search_dialog.open()

    # Найти населенный пункт
    text_search_dialog.find_location("Москва")
