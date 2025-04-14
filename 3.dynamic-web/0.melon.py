from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()

URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)

# song_info = driver.find_element(By.CSS_SELECTOR, 'a.btn.song_info') # 데이터 하나 찾음
song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')
# print(len(song_info))

song_list = []

for i in range(2):
    song_info[i].click()
    time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    # print(title)
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist span').text # 공란 >> div 태그 안에 있는 span , find element > 요소에 부합하는 첫번째
    
    # # 여러개를 찾은 다음 인덱스 접근
    # meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd')
    # print(meta_data[1].text)

    # 빌매일 정보를 특정
    publish_date = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
    like_ent = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    like_ent = like_ent.replace(',','')


    song_list.append([title, artist, publish_date, like_ent])

    driver.back()

local_file_path = '/home/ubuntu/damf2/data/melon/'

def save_to_csv(song_list):
    with open(local_file_path + 'melon-top-100.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(song_list)

save_to_csv(song_list)

