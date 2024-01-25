import time
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# 1-1. navigation 관련 tools
driver.get("http://www.naver.com")
time.sleep(1)
driver.get("http://www.google.com")

# 1-2. back() : 뒤로가기
driver.back()
time.sleep(1)

# 1-3. forward() : 앞으로가기
driver.forward()
time.sleep(1)   

# 1-4. refresh() : 새로고침
driver.refresh()
time.sleep(1)

# 1-5. quit() : 종료
driver.quit()
time.sleep(1)


driver.get("https://naver.com")
# 2-1. browser infomation
title = driver.title
print(title, "이 타이틀이다.")
