import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용
from selenium.webdriver.support.ui import WebDriverWait #class WebDriverWait 사용
from selenium.webdriver.support import expected_conditions as EC #class EC 사용

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

query = "python flask"
# search_link = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}"
search_link = f"https://search.naver.com/search.naver?query={query}&nso=&where=view&sm=tab_nmr"

driver.get(search_link)

# target_blog_link = "https://blog.naver.com/zlatmgpdjtiq/223049716285"
target_blog_link = "https://blog.naver.com/cheerfuldong/222694578203"
link_selector = f'a[href^="{target_blog_link}"]'
now_rank = -1

try:
    element = driver.find_element(By.CSS_SELECTOR, link_selector)
except:
    print("Element not found")
    driver.quit()

     
BLOG_FOUND = False
for _ in range(7):
    try:
        while True:
            new_element = element.find_element(By.XPATH, "./..")
            now_element = new_element.get_attribute("data-cr-rank")
            if now_element != None:
                print("현재랭크 찾음 :", now_element)
                BLOG_FOUND = True
                break
            print("현재랭크 못 찾음")
            element = new_element
        if BLOG_FOUND:
            break
    except:
        print("타겟 블로그를 못 찾음 > 스크롤 하겠습니다.")
        # driver.execute_script("window.scrollBy(0, 100)")
        time.sleep(3)
    print(f"{query} / {now_rank} : 타켓 블로그의 링크를 찾았습니다.")
    
input()