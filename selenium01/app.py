import time
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("http://www.naver.com")
time.sleep(1)

css_selecter = "#shortcutArea > ul" #copy selector
group_aavigator = driver.find_element(By.CSS_SELECTOR, css_selecter)

print(group_aavigator.text)

input()
