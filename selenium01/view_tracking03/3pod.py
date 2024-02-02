from selenium import webdriver
from PIL import Image
import pytesseract
import io
import requests
import time
from selenium.webdriver.common.by import By


# 웹 드라이버를 초기화합니다.
driver = webdriver.Chrome()

# 웹 페이지를 불러옵니다.
driver.get('http://sinbiweb-cloud.3-pod.com/')
time.sleep(20)

# 이미지 요소를 찾습니다.
image_element = driver.find_element(By.ID, 'QuestImage')

# 이미지 URL을 가져옵니다.
image_url = image_element.get_attribute('src')

# 이미지를 불러옵니다.
response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))

# 이미지에서 텍스트를 인식합니다.
text = pytesseract.image_to_string(image)

# 인식된 텍스트에서 숫자를 추출합니다.
numbers = [int(s) for s in text.split() if s.isdigit()]

print(numbers)

# # 인식된 숫자를 더합니다.
# total = sum(numbers)

# # input 태그를 찾습니다.
# input_element = driver.find_element_by_id('input_id')

# # input 태그에 값을 입력합니다.
# input_element.send_keys(str(total))

# # 웹 드라이버를 종료합니다.
# driver.quit()
