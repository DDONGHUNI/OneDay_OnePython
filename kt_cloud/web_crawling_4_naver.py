import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.naver.com'

keyword = "보안 회사"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(By.CLASS_NAME, "search_input").send_keys(f"{keyword}\n")
time.sleep(3) # 에러 발생할 수 있어 3초 대기

# 첫 번째 방법 : click event 를 주고 블로그 탭을 들어가는법
# driver.find_element(By.LINK_TEXT, "블로그").click()

# 두 번째 방법
driver.get(f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keyword}")

# 1. PAGE DOWN (키)

for i in range(1, 10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# 제목 불러오기
blog_elements = driver.find_elements(By.CLASS_NAME, "Pcw4FFPrGxhURyUmBGxh")

csv_data = []
for blog_i, blog_element in enumerate(blog_elements, start=1):
    blog_title = blog_element.text
    blog_url = blog_element.get_attribute('href')
    row_tuple = (blog_title, blog_url)
    csv_data.append(row_tuple)
    print(blog_i, row_tuple)

with open("data.csv", "w", encoding='utf-8-sig') as fw:
    
    for row_i, row in enumerate(csv_data):
        fw.write(f"{row_i},{row[0]},{row[1]}\n")

input()