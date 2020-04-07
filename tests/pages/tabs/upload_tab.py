from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ...helpers.w2ui_helper import W2UiHelper

explicit_wait = 10  # сек
explicit_wait_for_upload = 3600  # длительная задержка по умолчанию для загрузки (1 час)


class UploadTab:
    def __init__(self, driver):
        self.driver = driver
        self.w2ui_helper = W2UiHelper(self.driver)
        self.data_groups_map = {'maps': 6, 'mtw': 4, 'rsw': 5, 'rsc': 12, 'tiles': 14, 'PVO': 13, 'documents': 11}
        self.format_data = {'classif': 'Классификаторы'}

    def open(self):
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'tabs_tabsLeftPanel_tab_tabUploads'))).click()

    def upload_files(self, files, timeout=None):
        # Открыть панель "Загрузка файлов"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'titleDataUploadAndSave'))).click()

        # Заполнить таблицу файлами
        WebDriverWait(self.driver, explicit_wait).until(EC.presence_of_element_located((By.ID, 'file'))).send_keys(files)

        # Подождать, пока пропадет спиннер
        try:
            spinner = WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'w2ui-lock-msg')))

            # По умолчанию ждать завершения загрузки длительное время
            spinner_timeout = timeout
            if spinner_timeout is None:
                spinner_timeout = explicit_wait_for_upload
            WebDriverWait(self.driver, spinner_timeout).until(EC.staleness_of(spinner))
        except:
            print('Spinner was not handled')

    def send_to_storage(self):
        # Выбрать секцию "Помещение в хранилище"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'titleDataSaveInStorage'))).click()

        # Нажать кнопку "Поместить в хранилище"
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'btn_SaveInStorage'))).click()

    # выбрать позицию "Группа данных"
    def select_data_group(self, data_group):
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'inDataGroup')))
        self.w2ui_helper.select_field_value_by_id('inDataGroup', self.data_groups_map[data_group])

    # выбрать позицию "Формат данных"
    def select_format_data(self, formatData):
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'inFormatData')))
        self.w2ui_helper.select_field_value_by_id('inFormatData', self.format_data[formatData])

    # выбрать путь к загрузке данных
    def set_upload_path(self, upload_path):
        WebDriverWait(self.driver, explicit_wait).until(EC.element_to_be_clickable((By.ID, 'inpDataSaveFolder')))

        # Добавить и выбрать новый каталог для загрузки с сервера
        self.w2ui_helper.append_field_value_by_id('inpDataSaveFolder', upload_path)
        self.w2ui_helper.select_field_value_by_id('inpDataSaveFolder', upload_path)