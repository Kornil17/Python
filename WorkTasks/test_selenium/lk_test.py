import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://lk-test.egais.ru/cabinet/egais-services/corrections/")
driver.execute_script("window.localStorage.setItem('lk-test.egais.ru_lk-egais','Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZGV2ZWxvcGVyIiwiZmlyc3ROYW1lIjoi0KLQtdGB0YLQuNGA0L7QstGJ0LjQuiIsImxhc3ROYW1lIjoiKNCg0LDQt9GA0LDQsdC-0YLRh9C40LopIiwibG9jYWxpdHkiOiLQk9Ce0KDQntCUINCc0J7QodCa0JLQkCIsInJlZ2lvbiI6Ijc3IiwicmVnaW9uQ29kZSI6Ijc3IiwidXNlcmlkIjoiMjg5IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiIyODkiLCJyb2xlaWQiOiIxMiIsInBlcm1pc3Npb25zIjoiVXNlcnMsUm9sZXMsU3RhdGlzdGljYWxJbmYsQ29uc3VtcHRpb24sUmV0YWlsLE1hcmtldFBhcnRpY2lwYW50cyxNYXJrZXRQYXJ0aWNpcGFudHNWMixSZXBvcnRzLE9yZ2FuaXphdGlvbnMsUmVwb3J0VGVtcGxhdGVzLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFN0YXRpc3RpY2FsSW5mLFN0YXRpc3RpY2FsSW5mLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCIsImxpc3RSZWdpb25Db2RlcyI6Ijc3IiwiZXhwIjoxNjk5OTUzOTQxLCJpc3MiOiJDQUVnYWlzIiwiYXVkIjoiVXNlcnMifQ.YKJZFsJMHmV_R4GknnuosqeMpNlVkoykIPRBKPnmCeg');")
x = driver.execute_script("return window.localStorage;")
print(x)
# driver.refresh()
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[0])
# driver.get("https://lk-test.egais.ru/cabinet/egais-services/corrections/")
driver.get("https://lk-test.egais.ru/cabinet/licenses")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, "/html/body/app-root/app-cabinet-layout/app-layout/div/div/app-license-start-page/app-license-box-body/div/div[2]/div/div[1]/span").click()
time.sleep(5)
driver.close()

