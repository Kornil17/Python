import logging
from time import sleep

from flask import jsonify
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s ... %(name)s: %(message)s')
extension_path = r'./chrome_extensions/centrinform/extension.crx'
cr_opt = Options()
cr_opt.add_extension(extension_path)


class LocalStorage:
    """Base class to get a local storage of Google Chrome"""

    def __init__(self, driver):
        """set the driver to use for Chrome storage"""
        self.driver = driver

    def __len__(self):
        """return the number of items in the storage"""
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self):
        """return the pairs in the storage"""
        return self.driver.execute_script("var ls = window.localStorage, items = {}; "
                                          "for (var i = 0, k; i < ls.length; ++i) "
                                          "  items[k = ls.key(i)] = ls.getItem(k); "
                                          "return items; ")

    def keys(self):
        """return only the keys in the storage"""
        return self.driver.execute_script("var ls = window.localStorage, keys = []; "
                                          "for (var i = 0; i < ls.length; ++i) "
                                          "  keys[i] = ls.key(i); "
                                          "return keys; ")

    def get(self, key):
        """get value by key"""
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        """set or update value in storage"""
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        """return True if key in LocalStorage.keys()"""
        return key in self.keys()

    def remove(self, key):
        """remove pair by key in storage"""
        self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        """remove all items"""
        self.driver.execute_script("window.localStorage.clear();")

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()


class LcEgais:
    allowed_circuits = dict(test='lk-test.egais.ru', pred='pred-prod.egais.ru', prod='lk.egais.ru')


class LcLoginPage(LcEgais):
    password = '0987654321'

    class XPath:
        profile = '/html/body/app-root/app-login/app-layout-auth/div/app-auth-certificates/div/mat-accordion/mat' \
                  '-expansion-panel/mat-expansion-panel-header/span[1]/mat-panel-title'
        password = '/html/body/app-root/app-login/app-layout-auth/div/app-auth-certificates/div/mat-accordion/mat-' \
                   'expansion-panel/div/div/mat-panel-description/div[3]/mat-form-field/div/div[1]/div/input'
        confirm = '/html/body/app-root/app-login/app-layout-auth/div/app-auth-certificates/div/mat-accordion/mat' \
                  '-expansion-panel/div/div/mat-panel-description/div[3]/button/span[1]'


class BrowserExceptions:
    class PageUnavailable(Exception):
        pass

    class ElementNotFound(Exception):
        pass


class Browser:

    def __init__(self):
        chromedriver_autoinstaller.install(cwd=True)
        self.browser = webdriver.Chrome(options=cr_opt)
        self.storage = LocalStorage(self.browser)
        self.log = logging.getLogger('Browser')

    @staticmethod
    def delay(seconds):
        [sleep(1) for _ in tqdm(range(seconds))]

    def close(self):
        self.browser.close()

    def __login(self, url):
        try:
            self.browser.get(url)
        except Exception as _ex:
            self.log.error('Could not login: cause page is unavailable')
            self.log.error(_ex)
            raise BrowserExceptions.PageUnavailable()
        self.delay(5)

        try:
            self.browser.find_element(By.XPATH, LcLoginPage.XPath.profile).click()
        except NoSuchElementException as _ex:
            self.log.error('Could not login: cause Element PROFILE not found')
            self.log.error(_ex)
            raise BrowserExceptions.ElementNotFound()
        self.delay(2)

        try:
            self.browser.find_element(By.XPATH, LcLoginPage.XPath.password).send_keys(LcLoginPage.password)
        except Exception as _ex:
            self.log.error('Could not login: cause Element PASSWORD not found, or is not [@type=input]')
            self.log.error(_ex)
            raise BrowserExceptions.ElementNotFound()
        self.delay(2)

        try:
            self.browser.find_element(By.XPATH, LcLoginPage.XPath.confirm).click()
        except NoSuchElementException as _ex:
            self.log.error('Could not login: cause Element CONFIRM [@type=button] not found')
            self.log.error(_ex)
            raise BrowserExceptions.ElementNotFound()
        self.delay(10)
        return self.__get_local_storage()

    def __get_local_storage(self):
        self.log.debug(f'Data in local storage: \n {jsonify((data := self.storage.items()))}')
        return data

    def get_storage(self, circuit):
        if circuit not in LcEgais.allowed_circuits:
            return f"Circuit [{circuit}] is not allowed"

        self.log.debug(f'Current circuit: {circuit}')
        self.log.info((url := f'https://{LcEgais.allowed_circuits[circuit]}/cabinet/dashboard'))
        self.browser.get(url)
        self.delay(3)

        self.log.info(f'Logged in: {(logged := not self.browser.current_url.endswith("not_logged_in"))}')

        if not logged: return self.__login(self.browser.current_url)
        return self.__get_local_storage()
