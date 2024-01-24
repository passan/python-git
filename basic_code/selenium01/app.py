from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By #class by사용
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://naver.com")

selector = "#newsstand > div.ContentHeaderView-module__content_header___nSgPg > div > ul"
text_all = driver.find_element(By.CLASS_NAME, "ContentHeaderView-module__tab_list___BWrWe")

print(text_all.text)
input()
