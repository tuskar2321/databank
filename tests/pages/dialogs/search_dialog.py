import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

explicit_wait = 10  # sec

class SearchDialog:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # Нажать кнопку "Поиск"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'Поиск...')]"))).click()

    def set_data_name_search_type(self, search_type):
        search_field = WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='grid_map_operator_1']//*[contains(text(),'" + search_type + "')]")))
        self.driver.execute_script("arguments[0].setAttribute('selected', 'true')", search_field)

    def fill_data_name(self, data_name):
        WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located((By.ID, "grid_map_field_1"))).send_keys(data_name)

    def find(self):
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Найти')]"))).click()

        time.sleep(3)
