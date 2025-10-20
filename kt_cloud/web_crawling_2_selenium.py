import re
from selenium import webdriver

# --- 설정 ---
url = 'https://ipipip.kr'
driver = webdriver.Chrome()

# --- 웹 페이지 접속 및 소스 가져오기 ---
driver.get(url)
html_code = driver.page_source
driver.quit() # 브라우저 자원 해제

# --- 정규식 처리 ---
# IPv4 주소 패턴: 0.0.0.0 형태를 정확히 지정합니다.
# (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) :
#   - \d{1,3} : 1~3자리 숫자 (0부터 255까지의 숫자를 표현)
#   - \. : 문자 그대로의 점(.) (점은 정규식에서 특수문자이므로 이스케이프해야 함)
#   - 괄호 () : 추출할 문자열(캡처 그룹)을 지정합니다.
IP_REGEX = r'data-clipboard-text="(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"'

regrex_pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
m = regrex_pattern.search(html_code)
ip_address = m.group()
print(f"✅ 정규식으로 추출된 IP 주소: {ip_address}")
