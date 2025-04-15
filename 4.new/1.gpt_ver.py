from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

URL = 'https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111'
driver.get(URL)

# 페이지 로딩이 완료될 때까지 대기
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.list_content > a"))
)

# 인기 뉴스 리스트 가져오기
top_news = driver.find_elements(By.CSS_SELECTOR, "div.list_content > a")

# 뉴스 제목을 저장할 리스트
news_list = []

# 상위 2개의 뉴스 제목 클릭 후 추출
for el in range(5):
    # 각 뉴스 클릭
    top_news[el].click()

    # 뉴스 제목이 로드될 때까지 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.media_end_head_headline'))
    )

    # 제목 추출
    title = driver.find_element(By.CSS_SELECTOR, 'h2.media_end_head_headline')
    news_list.append(title.text)
    print(title.text)

    # 뒤로 가기
    driver.back()

    # 다시 페이지가 로드될 때까지 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.list_content > a"))
    )
    # 새로 로드된 뉴스 목록을 갱신
    top_news = driver.find_elements(By.CSS_SELECTOR, "div.list_content > a")

# 브라우저 종료
driver.quit()

# 추출된 뉴스 제목 목록
print("추출된 뉴스 제목들:", news_list)
