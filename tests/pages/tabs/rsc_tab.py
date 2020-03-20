from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

explicit_wait = 10  # sec


class RscTab:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # Открыть страницу "Данные"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'tabs_tabsLeftPanel_tab_tabDBData'))).click()

        # Открыть страницу "Классификаторы"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'tabs_tabletabs_tab_rscs'))).click()

    def is_record_exist_by_name(self, record_name):
        WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "100t05gm.rsc")]')))

        found_records = self.driver.find_elements_by_css_selector('tr div[title="Наименование"]')
        print(found_records)
        for record in found_records:
            if record.text == record_name:
                return True

    # Скачивание данных
    def download_raster(self, record_name):
        self.driver.find_element_by_xpath("//div[starts-with(text(),'" + record_name + "')]/../following-sibling::td//a[contains(@class, 'fa-download')]").click()

    def select_record_by_name(self, record_name):
        found_records = self.driver.find_elements_by_css_selector('tr div[title="Наименование"]')
        for record in found_records:
            if record.text == record_name:
                record.click()
                return True
