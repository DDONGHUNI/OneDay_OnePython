from selenium import webdriver

url = 'https://ipipip.kr'

driver = webdriver.Chrome()
driver.get(url)
html_code = driver.page_source
driver.quit()

html_code_line_list = html_code.split('\n')

for html_code_line in html_code_line_list:
    if html_code_line.find("data-clipboard-text") >= 0:
        print(html_code_line)
        cut_line = html_code_line
        break

clipboard_len = len("data-clipboard-text")
cut_line = cut_line[cut_line.find("data-clipboard-text")+clipboard_len+2:]
cut_line2 = cut_line[:cut_line.find("\"")]
print(f"✅ 추출된 IP 주소: {cut_line2}")