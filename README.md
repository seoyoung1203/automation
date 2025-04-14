# cron
- cron tab 등록
```shell
crontab -e
```
i -> insert 모드
esc -> 탈출
:wq -> 종료

- cron 리스트 확인
```shell
crontab -l
```

- 기본문법

* * * * * <실행할 명령어>

분(0-59),시(0-23),일(1-31),월(1-12),요일(0-6) (정보) >> * -> 매분마다 실행할게염

1. upload_to_hdfs.py
```shell
pip install hdfs
```
파이썬 명령어로 접속 가능

- client.content('/input') >> 폴더 안에 리스트 보여줌

- beautifulsoup : 웹 페이지에서 원하는 정보를 쉽게 파싱(구조 분해) 할 수 있게 도와주는 라이브러리


-------------
## dynamic-web
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo apt --fix-broken install -y : 설치 위해서 필요한 프로그램 설치해주세요

sudo dpkg -i google-chrome-stable_current_amd64.deb

### copy > copy selector

- li:nth-of-type() >> 몇 번째 li 태그를 선택할지 지정
    cf) li:first-child
- p:not(.foo) >> 특정한 상황 제외하고 아닌 친구 뽑아줌
- li:nth-of-type(2n+3)(수식) >> 원하는 특정 데이터 반복 찾기
- div>* div >> 태그 안에 있는 모든 자식 요소 가져오세요
- span[data-item] >> data-item이라고 하는 arrtibute를 가진 데이터 뽑기
- p ~ span >> p와 동등한 level에 있는 span 태그 가져오기 (형제 선택자)
- :enabled >> disabled가 없는 애들 
- #one,#two,#six,#nine >> 내가 원하는 요소의 지정된 id 값으로 가져오기 
- a + 
- div#foo > div.foo >> 부모 먼저 고르고 하위 선택
- div(위) div(그 안) span + code:not(.foo) >> span 태그의 형제인 태그들 > 