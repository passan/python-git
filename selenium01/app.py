import time
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# 1. 웹 브라우저 주소창을 컨트롤하기 driver.get
driver.get("http://www.naver.com")
time.sleep(1)

# 2-1. 요소를 찾아서 Copy 해옴. 실제 웹 브라우저 개발자 도수로 찾아서 사용해야함.
css_selecter = "#shortcutArea > ul" #copy selector

# 2-2. 찾아온 요소를 find_element로 가져오기
group_navigator = driver.find_element(By.CSS_SELECTOR, css_selecter)

# 3-1. 데이터를 가져오기
print(group_navigator.text)

# 3-2. 요소를 클릭하기(중앙)
group_navigator.click()
input()
