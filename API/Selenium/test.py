from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://www.linuxhint.com')
print('Title: %s' % browser.title)
browser.quit()
