import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..pages.home_page import HomePage


def test_load_rsc():
    driver = webdriver.Chrome()

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Проверить наличие классификаторов в списке
    rsc_tab = home_page.get_rsc_tab()
    rsc_tab.open()

    record_names = ['100t05gm.rsc', '200t05gm.rsc']
    for record_name in record_names:
        assert rsc_tab.is_record_exist_by_name(record_name)
        
    # Скачать тестовый набор данных
    rsc_tab.download_raster(record_names[0])
    time.sleep(10) # FIXME

    # Проверить наличие скачанного файла на диске
    acrhive_path = glob.glob(os.path.join(pathlib.Path.home(), 'Downloads', '*100t05gm.rsc.zip'))
    time.sleep(5)  # FIXME
    assert os.path.exists(acrhive_path[0])

    # time.sleep(60)
