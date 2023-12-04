import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Test:
    driver = webdriver.Firefox()
    def test_main(self):
        self.driver.get('http://utm-feature.middleware.monitor-utm.ru/app/services/brewers-registry/list')
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-list/app-table-view-wrapper/div/button').click()
        time.sleep(5)
        # self.driver.close()
    def test_fist_page(self):
        self.driver.find_element(By.XPATH,"//*[@id='mat-input-2']").send_keys('1232132132132')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-3']").send_keys('test@mail.ru')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-4']").send_keys('8888888888')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-5']").send_keys('1234')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-6']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-month-view/table/tbody/tr[4]/td[2]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-stepper/form/div/button[2]").click()
        time.sleep(5)
        # self.driver.close()
    def test_second_page(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-stepper/form/mat-horizontal-stepper/div[2]/div[2]/mat-radio-group/div[1]/mat-radio-button/label/span[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-stepper/form/div/button[2]").click()
        # self.driver.close()

    def test_third_page(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="mat-select-value-7"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="mat-option-16"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-22"]').send_keys('999')
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-23"]]').send_keys('14:41:4141414:141')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-stepper/form/mat-horizontal-stepper/div[2]/div[3]/app-subdivision-array/app-array-view/mat-accordion/mat-expansion-panel/div/div/mat-card/mat-card-content/app-inclusion-subdivision-container/div/app-brewers-subdivision/div/app-list-view[1]/mat-accordion/mat-expansion-panel/div/div/ul/li/div[1]/div[2]/mat-form-field/div/div[1]/div").send_keys('123')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-stepper/form/mat-horizontal-stepper/div[2]/div[3]/app-subdivision-array/app-array-view/mat-accordion/mat-expansion-panel/div/div/mat-card/mat-card-content/app-inclusion-subdivision-container/div/app-brewers-subdivision/div/app-list-view[1]/mat-accordion/mat-expansion-panel/div/div/ul/li/div[1]/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button/span[1]/svg").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[11]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-month-view/table/tbody/tr[4]/td[3]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='mat-select-value-11']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/main/app-brewers-registry-stepper/form/mat-horizontal-stepper/div[2]/div[3]/app-subdivision-array/app-array-view/mat-accordion/mat-expansion-panel/div/div/mat-card/mat-card-content/app-inclusion-subdivision-container/div/app-brewers-subdivision/div/app-list-view[2]/mat-accordion/mat-expansion-panel/div/div/ul/li/div[1]/mat-form-field[2]/div/div[1]/div").send_keys('1231')
        self.driver.close()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "").click()
        time.sleep(2)
        self.driver.close()


