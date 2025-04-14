from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = 'https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111'
driver.get(URL)

time.sleep(5)

top_news = driver.find_elements(By.CSS_SELECTOR, "div.list_content > a")

news_list = []

for el in range(2):
    top_news[el].click()


    title = driver.find_element(By.CSS_SELECTOR, 'a.list_title')
    print(title)
    
