import requests
from bs4 import BeautifulSoup

lotto_url = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser')

balls = soup.select('span.ball_645') # 찾고 싶은 데이터의 공통 조건 찾기
for ball in balls:
    print(ball.text)
