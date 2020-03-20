import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..helpers.waiter import Waiter
from ..pages.home_page import HomePage
from ..pages.dialogs.search_dialog import SearchDialog


def test_load_maps():
    # Сформировать пустой каталог для загрузки
    download_full_path = FilePath.create_downloads_dir_with_erase('test_load_maps')
    chrome_options_with_download_path = webdriver.ChromeOptions()
    chrome_options_with_download_path.add_experimental_option("prefs", {"download.default_directory" : download_full_path})

    # Открыть браузер
    driver = webdriver.Chrome(chrome_options=chrome_options_with_download_path)

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Открыть вкладку "Загрузка материалов"
    upload_tab = home_page.get_upload_tab()
    upload_tab.open()
    upload_tab.select_data_group('maps')

    # Загрузить файлы во временное хранилище
    upload_files_list = FilePath.form_full_test_data_path(['sxf/O361.sxf', 'sxf/O362.sxf'])
    upload_tab.upload_files(upload_files_list)

    # Загрузить файлы в постоянное хранилище
    upload_tab.send_to_storage()

    # Проанализировать попап
    popup = home_page.wait_for_popup(10)  # sec
    assert popup.text.find('Ошибка') == -1  # не содержит
    home_page.close_popup()

    # Проверить наличие карты в списке
    maps_tab = home_page.get_maps_tab()
    maps_tab.open()

    # Установить фильтр на таблицу
    search_dialog = SearchDialog(driver)
    search_dialog.open()
    search_dialog.set_data_name_search_type('равняется')
    search_dialog.fill_data_name('0.O-36-1')
    search_dialog.find()

    record_names = ['0.O-36-1']
    for record_name in record_names:
        assert maps_tab.is_record_exist_by_name(record_name)

    # Скачать тестовый набор данных
    maps_tab.download_found_map(record_names[0])

    # Проверить наличие скачанного файла на диске
    acrhive_path_glob = os.path.join(download_full_path, '*O361.sxf.zip')
    Waiter.wait_file_download_by_glob(acrhive_path_glob)
