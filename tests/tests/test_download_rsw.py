import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..pages.home_page import HomePage
from ..helpers.waiter import Waiter


def test_download_rsw():
    driver = webdriver.Chrome()

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Проверить наличие растра в списке
    raster_tab = home_page.get_raster_tab()
    raster_tab.open()

    record_names = ['O350251.rsw', 'O350252.rsw']
    for record_name in record_names:
        assert raster_tab.is_record_exist_by_name(record_name)
        
    # Скачать тестовый набор данных
    raster_tab.download_raster(record_names[0])

    # Проверить наличие скачанного файла на диске
    acrhive_path_glob = os.path.join(pathlib.Path.home(), 'Downloads', '*O350251.rsw.zip')
    Waiter.wait_file_download_by_glob(acrhive_path_glob)

    # time.sleep(60)
