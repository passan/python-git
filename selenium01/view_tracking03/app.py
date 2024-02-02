import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용
from selenium.webdriver.support.ui import WebDriverWait #class WebDriverWait 사용
from selenium.webdriver.support import expected_conditions as EC #class EC 사용

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

seach_query = "부산피부과"
search_link = f"https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={seach_query}"
driver.get(search_link)



view_selector = "a.YORrF"
plays_more_element = driver.find_element(By.CSS_SELECTOR, view_selector)
print(plays_more_element.text)
plays_more_element.click()

time.sleep(3)
more_selector = "a.cf8PL"
plays_more_element = driver.find_element(By.CSS_SELECTOR, more_selector)
print(plays_more_element.text)
plays_more_element.click()


input()