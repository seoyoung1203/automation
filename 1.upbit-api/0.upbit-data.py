from datetime import datetime
import requests
import time
import csv

upbit_url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'

start_time = time.time()

bit_data_list = []

while time.time() - start_time < 60: # 현재 시간에서 과거의 시간을 빼는
    res = requests.get(upbit_url)
    data = res.json()[0]

    bit_data = [
        data['market'],
        data['trade_date'],
        data['trade_time'],
        data['trade_price']
    ]

    bit_data_list.append(bit_data)
    time.sleep(10)

    # print(bit_data_list)

local_file_path = '/home/ubuntu/damf2/data/bitcoin/' # 고정값

now = datetime.now()
file_name = now.strftime('%H-%M-%S') + '.csv' # datetime 객체를 글자로 바꾸기 # 타이밍마다 변함

with open(local_file_path + file_name, mode='w', newline='') as file: # open >> 특정 os 경로의 파일을 열어 file이라는 변수에 저장
    writer = csv.writer(file)
    writer.writerows(bit_data_list)


