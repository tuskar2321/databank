import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..pages.home_page import HomePage


def test_download_mtw():
    driver = webdriver.Chrome()

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Проверить наличие матрицы в списке
    matrix_tab = home_page.get_matrix_tab()
    matrix_tab.open()

    record_names = ['0.O-36-051.mtw', '0.O-36-052.mtw']
    for record_name in record_names:
        assert matrix_tab.is_record_exist_by_name(record_name)
        
    # Скачать тестовый набор данных
    matrix_tab.download_matrix(record_names[0])

    # Проверить наличие скачанного файла на диске
    acrhive_path = glob.glob(os.path.join(pathlib.Path.home(), 'Downloads', '*0.O-36-051.mtw.zip'))
    time.sleep(10)  # FIXME
    assert os.path.exists(acrhive_path[0])

    # time.sleep(30)
