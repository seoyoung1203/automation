# cron
- cron jab 등록
```shell
crontab -e
```

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