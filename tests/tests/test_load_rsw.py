import time
import os
import pathlib
import glob
from selenium import webdriver

from ..helpers.filepath import FilePath
from ..pages.home_page import HomePage


def test_load_rsw():
    # Сформировать пустой каталог для загрузки
    download_full_path = FilePath.create_downloads_dir_with_erase('test_load_rsw')
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
    upload_tab.select_data_group('rsw')

    # Загрузить файлы во временное хранилище
    upload_files_list = FilePath.form_full_test_data_path(['rsw/O350251.rsw', 'rsw/O350252.rsw'])
    upload_tab.upload_files(upload_files_list)

    # Загрузить файлы в постоянное хранилище
    upload_tab.send_to_storage()

    # Проанализировать попап
    popup = home_page.wait_for_popup(5)  # sec
    assert popup.text.find('Ошибка') == -1  # не содержит
    home_page.close_popup()

    # Проверить наличие матрицы в списке
    raster_tab = home_page.get_raster_tab()
    raster_tab.open()

    record_names = ['O350251.rsw', 'O350252.rsw']
    for record_name in record_names:
        assert raster_tab.is_record_exist_by_name(record_name)

    # Скачать тестовый набор данных
    raster_tab.download_raster(record_names[0])
    time.sleep(10)  # FIXME

    # Проверить наличие скачанного файла на диске
    acrhive_path = glob.glob(os.path.join(pathlib.Path.home(), 'Downloads', '*O350251.rsw.zip'))
    time.sleep(5)  # FIXME
    assert os.path.exists(acrhive_path[0])

    # time.sleep(1000)
