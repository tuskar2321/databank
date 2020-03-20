import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..pages.home_page import HomePage


def test_load_mtw():
    driver = webdriver.Chrome()

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Открыть вкладку "Загрузка материалов"
    upload_tab = home_page.get_upload_tab()
    upload_tab.open()
    upload_tab.select_data_group('mtw')

    # Загрузить файлы во временное хранилище
    upload_files_list = FilePath.form_full_test_data_path(['mtw/0.O-36-051.mtw', 'mtw/0.O-36-052.mtw'])
    upload_tab.upload_files(upload_files_list)

    # Загрузить файлы в постоянное хранилище
    upload_tab.send_to_storage()

    # Проанализировать попап
    popup = home_page.wait_for_popup(5)  # sec
    assert popup.text.find('Ошибка') == -1  # не содержит
    home_page.close_popup()

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
    time.sleep(5)  # FIXME
    assert os.path.exists(acrhive_path[0])

    # time.sleep(1000)
