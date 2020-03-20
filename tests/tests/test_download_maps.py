import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..pages.home_page import HomePage

def test_download_maps():
    driver = webdriver.Chrome()

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()
    time.sleep(3)  # FIXME

    # Проверить наличие карты в списке
    maps_tab = home_page.get_maps_tab()
    record_names = ['0.O-36-1', '0.O-36-2']
    for record_name in record_names:
        assert maps_tab.is_record_exist_by_name(record_name)

    # Скачать тестовый набор данных
    maps_tab.download_map(record_names[0])

    # Проверить наличие скачанного файла на диске
    acrhive_path = glob.glob(os.path.join(pathlib.Path.home(), 'Downloads', '*O361.sxf.zip'))
    time.sleep(10)  # FIXME
    assert os.path.exists(acrhive_path[0])

    time.sleep(50)