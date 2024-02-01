import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용
from selenium.webdriver.support.ui import WebDriverWait #class WebDriverWait 사용
from selenium.webdriver.support import expected_conditions as EC #class EC 사용

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

query = ["python flask","selenium"]
target_blog_link = ["https://blog.naver.com/zilly1/223081405563", "https://blog.naver.com/swimmingsdesign/223034723268"]

for query, target_blog_link in zip(query, target_blog_link):    
    search_link = f"https://search.naver.com/search.naver?query={query}&nso=&where=view&sm=tab_nmr"
    driver.get(search_link)
    time.sleep(2)

    link_selector = f'a[href^="{target_blog_link}"]'
    now_rank = -1

    try:
        element = driver.find_element(By.CSS_SELECTOR, link_selector)
    except:
        print("Element not found")
        # driver.quit()

        
    BLOG_FOUND = False
    for _ in range(6):
        if BLOG_FOUND:
            break
        try:
            while True:
                new_element = element.find_element(By.XPATH, "./..")
                now_element = new_element.get_attribute("data-cr-rank")
                if now_element != None:
                    # print("현재랭크 찾음 :", now_element)
                    now_rank = now_element  # 현재 순위를 now_rank 변수에 저장
                    BLOG_FOUND = True
                    break
                print("현재랭크 못 찾음")
                element = new_element
        except:
            # print("타겟 블로그를 못 찾음 > 스크롤 하겠습니다.")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")            
            time.sleep(5)
        if BLOG_FOUND:
            print(f"{query} / {now_rank}: 타켓 블로그의 링크를 찾았습니다.")
            break  # 블로그의 순위를 찾은 후에 외부 for문을 종료
   
input()