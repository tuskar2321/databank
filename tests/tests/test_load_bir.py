import os
import posixpath

from selenium import webdriver

from ..helpers.git_helper import GitHelper
from ..helpers.params_registry import ParamsRegistry
from ..pages.home_page import HomePage


def test_load_bir_from_data_folder():
    # Склонировать или обновить тестовые данные на сервере
    git_helper = GitHelper(ParamsRegistry.test_data_repo_remote_path())
    remote_data_path = posixpath.join(ParamsRegistry.geodbse_upload_data_path(), 'geodbse-test-data')
    git_helper.clone_or_reset_via_ssh(ParamsRegistry.remote_host(), ParamsRegistry.ssh_user(), ParamsRegistry.ssh_password(), remote_data_path)

    # Открыть браузер
    driver = webdriver.Chrome()

    # Открыть домашнюю страницу
    home_page = HomePage(driver)
    home_page.open()

    # Открыть вкладку "Загрузка материалов"
    upload_tab = home_page.get_upload_tab()
    upload_tab.open()

    # Добавить в список новый каталог загрузки
    upload_tab.set_upload_path('geodbse-test-data/data/sxf')  # FIXME

    # Загрузить файлы в постоянное хранилище
    upload_tab.send_to_storage()

    # TODO
    time.sleep(1000)
