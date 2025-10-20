# https://www.free-webproxy-list.kr/ 프록시 리스트만 가져오는 코드

import re
from selenium import webdriver

url = 'https://www.free-webproxy-list.kr'
driver = webdriver.Chrome()
driver.get(url)

html_code = driver.page_source
driver.quit()

# regex_pattern = re.compile('https\:\/\/(\w+[-]*\.){1,}\w+')
#1. : / > 특수문자는 escape (\)
regrex_pattern = re.compile('https\:\/\/([a-z-0-9]+\.){0,}[a-z-0-9]+')
output = regrex_pattern.finditer(html_code)

for domain in output:
    print(domain)