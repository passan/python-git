# 필요한 모듈들을 임포트합니다.
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By # By 클래스를 사용하기 위해 임포트합니다.
from selenium.webdriver.support.ui import WebDriverWait # WebDriverWait 클래스를 사용하기 위해 임포트합니다.
from selenium.webdriver.support import expected_conditions as EC # EC 클래스를 사용하기 위해 임포트합니다.

# 크롬 드라이버를 자동으로 설치합니다.
chromedriver_autoinstaller.install()

# 크롬 웹드라이버 객체를 생성합니다.
driver = webdriver.Chrome()

# 검색할 쿼리와 대상 블로그 링크를 리스트로 정의합니다.
query = ["python flask","selenium"]
target_blog_link = ["https://blog.naver.com/zilly1/223081405563", "https://blog.naver.com/masichyun77/223202909929"]

# 각 쿼리와 대상 블로그 링크에 대해 반복합니다.
for query, target_blog_link in zip(query, target_blog_link):    
    # 네이버에서 쿼리를 검색하는 URL을 생성합니다.
    search_link = f"https://search.naver.com/search.naver?query={query}&nso=&where=view&sm=tab_nmr"
    # 웹드라이버로 해당 URL을 엽니다.
    driver.get(search_link)
    # 2초 동안 대기합니다.
    time.sleep(2)

    # 대상 블로그 링크를 선택하는 CSS 선택자를 생성합니다.
    link_selector = f'a[href^="{target_blog_link}"]'
    # 현재 순위를 저장할 변수를 초기화합니다.
    now_rank = -1

    # 해당 선택자로 웹 요소를 찾습니다.
    try:
        element = driver.find_element(By.CSS_SELECTOR, link_selector)
    except:
        # 웹 요소를 찾지 못하면 에러 메시지를 출력합니다.
        print(f"Element not found for {query} and {target_blog_link}")
        # driver.quit()

    # 블로그를 찾았는지 여부를 저장할 변수를 초기화합니다.
    BLOG_FOUND = False
    # 10번 반복합니다.
    for _ in range(10):
        # 블로그를 찾았다면 반복을 종료합니다.
        if BLOG_FOUND:
            break
        try:
            # 무한 반복합니다.
            while True:
                # 현재 웹 요소의 부모 요소를 찾습니다.
                new_element = element.find_element(By.XPATH, "./..")
                # 부모 요소의 'data-cr-rank' 속성 값을 가져옵니다.
                now_element = new_element.get_attribute("data-cr-rank")
                # 속성 값이 None이 아니라면,
                if now_element != None:
                    # 현재 순위를 now_rank 변수에 저장하고,
                    now_rank = now_element  
                    # 블로그를 찾았음을 표시하고,
                    BLOG_FOUND = True
                    # 무한 반복을 종료합니다.
                    break
                # 현재 웹 요소를 부모 요소로 변경합니다.
                element = new_element
        except:
            # 타겟 블로그를 찾지 못했다면 스크롤을 내립니다.
            print("타겟 블로그를 못 찾음 > 스크롤 하겠습니다.")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # driver.execute_script("window.scrollTo(0, 10000);")            
            # 5초 동안 대기합니다.
            time.sleep(5)
        # 블로그를 찾았다면,
        if BLOG_FOUND:
            # 쿼리와 현재 순위를 출력하고,
            print(f"{query} / {now_rank}: 타켓 블로그의 링크를 찾았습니다.")
            # 외부 for문을 종료합니다.
            break  
   
# 사용자의 입력을 기다립니다.
input()
