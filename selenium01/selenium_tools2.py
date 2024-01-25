import time
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get("https://naver.com")
# 2-1. browser infomation
title = driver.title
print(title, "이 타이틀이다.")

# 2-2. current_url 주소창을 그대로 가지고옴
driver.current_url
print(driver.current_url, "가 현재주소다")
