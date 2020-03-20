import os
import shutil


class FilePath:
    def form_full_test_data_path(relative_file_paths):
        # Получить значение переменной окружения CORE_LOCAL_TEST_DATA_DIR
        test_data_dir = os.environ['GEODBSE_LOCAL_TEST_DATA_DIR']
        assert test_data_dir

        # Сформировать массив с полными путями
        full_file_paths = os.path.join(test_data_dir, relative_file_paths[0])
        for relative_file_path in relative_file_paths[1:len(relative_file_paths)]:
            full_file_paths += '\n'
            full_file_paths += os.path.join(test_data_dir, relative_file_path)

        return full_file_paths

    form_full_test_data_path = staticmethod(form_full_test_data_path)

    def create_downloads_dir_with_erase(relative_download_path):
        # Получить значение переменной окружения CORE_LOCAL_TEST_DATA_DIR
        test_data_dir = os.environ['GEODBSE_LOCAL_TEST_DATA_DIR']
        assert test_data_dir

        # Сформировать полный путь до каталога скачивания
        download_full_path = os.path.join(test_data_dir, relative_download_path)
        # Очистить каталог, если существует
        if os.path.isdir(download_full_path) is True:
            shutil.rmtree(download_full_path)
        
        # Создать каталог
        os.mkdir(download_full_path)
        
        return download_full_path

    create_downloads_dir_with_erase = staticmethod(create_downloads_dir_with_erase)
            