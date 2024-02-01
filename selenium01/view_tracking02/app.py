import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By #class by사용
from selenium.webdriver.support.ui import WebDriverWait #class WebDriverWait 사용
from selenium.webdriver.support import expected_conditions as EC #class EC 사용

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

pagingindex = 2
seach_query = "꿀사과"
shoping_link = f"https://msearch.shopping.naver.com/search/all?query={seach_query}&vertical=search&pagingIndex={pagingindex}"
driver.get(shoping_link)

# 스크롤을 내립니다.
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# 상품 코드를 찾습니다.
try:
    target_code = "83450430618"
    target_selector = f"a[data-i='{target_code}']"
    target_element = driver.find_element(By.CSS_SELECTOR, target_selector)
    data = target_element.get_attribute("data-nclick")
    print(data)# 전체 상품 코드 출력
    print(data.split(f"{target_code},r:")) # 상품 코드 빼고 r을 기준으로 리스트를 만들어 출력 코드는 출력 안됨
    print(data.split(f"{target_code},r:")[-1]) # 리스트에 마지막 요소만 출력
    rank = (data.split(f"{target_code},r:")[-1].split(",")[0]) # 0번 인덱스 요소만 출력
    print("등수", rank) #현제 페이지 등수
    # real_rank = (int(pagingindex) - 1) * 40 + int(rank) #페이지별로 다시 순번이 안정해지기 때문에 사용 안함
    
except:
    print("상품 코드를 찾을 수 없습니다.")    



input()


# https://m.smartstore.naver.com/yg_apple/products/5905931130?NaPm=ct%3Dls2uimbs%7Cci%3D1922ec691fd187572a5e5ffa949bce994c871005%7Ctr%3Dslsl%7Csn%3D574561%7Chk%3D9c3562b99d9da56935fe3b183124e122e9cfe41f