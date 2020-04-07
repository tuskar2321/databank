import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

explicit_wait = 10  # sec


class TextSearchDialog:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # Нажать кнопку "Поиск"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, "panel_button_search"))).click()

    def find_location(self, location_name):
        WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located((By.ID, "inputSearchText"))).send_keys(location_name)
        self.driver.find_element_by_id("inputSearchButton").click()

        # Подождать popup с результатами поиска
        WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located((By.ID, "objPane")))
