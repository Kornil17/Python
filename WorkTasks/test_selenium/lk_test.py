import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://lk-test.egais.ru/cabinet/egais-services/corrections/")
driver.execute_script("window.localStorage.setItem('lk-test.egais.ru_lk-egais','Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZGV2ZWxvcGVyIiwiZmlyc3ROYW1lIjoi0JDQvdC00YDQtdC5INCt0YDQvdC10YHRgtC-0LLQuNGH0L7QstC40YciLCJsYXN0TmFtZSI6ItCR0YPQutC60LAiLCJsb2NhbGl0eSI6ItCT0J7QoNCe0JQg0JzQntCh0JrQktCQIiwicmVnaW9uIjoiNzciLCJyZWdpb25Db2RlIjoiNzciLCJ1c2VyaWQiOiIyODEiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjI4MSIsInJvbGVpZCI6IjEyIiwicGVybWlzc2lvbnMiOiJVc2VycyxSb2xlcyxTdGF0aXN0aWNhbEluZixDb25zdW1wdGlvbixSZXRhaWwsTWFya2V0UGFydGljaXBhbnRzLE1hcmtldFBhcnRpY2lwYW50c1YyLFJlcG9ydHMsT3JnYW5pemF0aW9ucyxSZXBvcnRUZW1wbGF0ZXMsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsU3RhdGlzdGljYWxJbmYsU3RhdGlzdGljYWxJbmYsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsIiwibGlzdFJlZ2lvbkNvZGVzIjoiNzciLCJleHAiOjE3MDA4MjQxNjIsImlzcyI6IkNBRWdhaXMiLCJhdWQiOiJVc2VycyJ9.v1upfMoUbGjOG_EPkC23WmZHzbUM685HlLstZ3o4c4k');")
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

