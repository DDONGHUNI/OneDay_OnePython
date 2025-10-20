from selenium import webdriver
from selenium.webdriver.common.by import By

def get_blog_content(url):
    url = 'https://blog.naver.com/coreit_gene/224028104274'
    driver.get(url)
    driver.switch_to.frame("mainFrame")
    blog_content = driver.find_element(By.CLASS_NAME, "se-main-container")
    blog_content = blog_content.text
    return blog_content

driver = webdriver.Chrome()

with open("data.csv", encoding='utf-8-sig') as fr:
    data_list = fr.readlines()
    blog_url_list = []
    for row in data_list:
        url = row.split(",")[-1].rstrip()
        blog_url_list.append(url)


with open("blog_content.csv", "w", encoding='utf-8-sig') as fw:
    for blog_i, blog_url in enumerate(blog_url_list):
        print(blog_i, blog_url)
        content = get_blog_content(blog_url)
        content = content.replace("\n", " ")
        try:
            fw.write(f"{blog_i},{content}\n")
        except:
            print("ERROR", blog_url)