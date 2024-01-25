import time
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용
from selenium.webdriver.support.ui import WebDriverWait #class WebDriverWait 사용
from selenium.webdriver.support import expected_conditions as EC #class EC 사용

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get("https://naver.com")

# 3. Driver Wait
# 3-1. 30초까지 기다리고 30초가 넘어가면 예외
css_selecter_error = "#shortcutArea > ux"
css_selecter = "#shortcutArea > ul"

try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selecter)))
except:
    print("예외 발생")
print("다음 코드 실행")


