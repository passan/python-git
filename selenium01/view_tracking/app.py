import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용
from selenium.webdriver.support.ui import WebDriverWait #class WebDriverWait 사용
from selenium.webdriver.support import expected_conditions as EC #class EC 사용

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

query = "python flask"
search_link = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}"

driver.get(search_link)

target_blog_link = "https://blog.naver.com/zlatmgpdjtiq/223049716285"
link_selector = f'a[href^="{target_blog_link}"]'

try:
    element = driver.find_element(By.CSS_SELECTOR, link_selector)
except:
    print("Element not found")
    driver.quit()
    
try:
    while True:
        new_element = element.find_element(By.XPATH, "./..")
        now_element = new_element.get_attribute("data-cr-rank")
        if now_element != None:
            print("현재랭크 찾음 :", now_element)
            break
        print("현재랭크 못 찾음")
        element = new_element
except:
    print("타겟 블로그를 못 찾음")
print(f"{query} : 타켓 블로그의 링크를 찾았습니다.")
    
input()