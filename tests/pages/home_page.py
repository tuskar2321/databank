import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .tabs.upload_tab import UploadTab
from .tabs.maps_tab import MapsTab
from .tabs.matrix_tab import MatrixTab
from .tabs.raster_tab import RasterTab
from .tabs.rsc_tab import RscTab

explicit_wait = 10  # sec


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.matrix_tab = MatrixTab(driver)
        self.raster_tab = RasterTab(driver)
        self.maps_tab = MapsTab(driver)
        self.upload_tab = UploadTab(driver)
        self.rsc_tab = RscTab(driver)
        
    def open(self):
        try:
            tagret_host = os.environ['HOST']
            self.driver.get('http://admin:admin@' + tagret_host + '/geodbse/?act=login')  
        except:
            self.driver.get('http://admin:admin@localhost/geodbse/geodbse/?act=login')  

    def get_maps_tab(self):
        return self.maps_tab

    def get_matrix_tab(self):
        return self.matrix_tab
    
    def get_raster_tab(self):
        return self.raster_tab

    def get_upload_tab(self):
        return self.upload_tab

    def get_rsc_tab(self):
        return self.rsc_tab

    def wait_for_popup(self, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, 'w2ui-popup')))

    def close_popup(self):
        # Нажать кнопку "Закрыть"
        close_button = WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#w2ui-popup .w2ui-msg-buttons')))
        close_button.click()

        # Подождать исчезновения кнопки "Закрыть"
        WebDriverWait(self.driver, explicit_wait).until(EC.staleness_of(close_button))
