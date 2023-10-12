from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Firefox()
    browser.get('https://www.google.com/')
    # click_entarance = browser.find_element(By.LINK_TEXT, "Войти").click()
    input_word = browser.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('hello\n')
    enter = browser.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(u'\ue007')
    sleep(5)
    click_video_by_xpath = browser.find_element(By.XPATH, "/html/body/div[5]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/div/div/a/div/div[2]/div[1]/div/span").click()
    sleep(20)
    browser.close()
finally:
    browser.quit()

