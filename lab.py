# 데이터 추출
from google.cloud import storage
import csv
import os

readtxt = open('C:/Users/jhbae/Downloads/player_info.txt', 'rt', encoding='UTF-8')
writetxt = open('C:/Users/jhbae/Downloads/player_info_wirte.txt', 'wt')
old_name = 'C:/Users/jhbae/Downloads/player_info_wirte.txt'
new_name = 'C:/Users/jhbae/Downloads/player_info_wirte.csv'
wirtecsv = open('player_data.csv', 'w')
wr = csv.writer(wirtecsv)

lines = readtxt.readlines()

cnt = 1

writetxt.write('num, name, position, team_name')
for line in lines:
    line = line.replace("등번호: ","")
    line = line.replace("이름: ","")
    line = line.replace("포지션: ","")
    line = line.replace("팀명: ","")
    line = line.strip()

    if(line == ''):
        line += '\n'

    if(cnt % 5 != 0 and line != '\n'):
        line = line + ','
        cnt += 1
        writetxt.write(line)
    else:
        cnt += 1
        writetxt.write(line)

    print(line)
readtxt.close()
writetxt.close()
os.rename(old_name, new_name)

# 로컬에서 버킷(TPCG-jh2)으로 player_info.txt 파일로 파일 전송

PROJECT_ID = 'tpcg-298808'
BUCKET_NAME = 'tpcg-jh'
BUCKET_NAME1 = 'tpcg-jh2'
storage_client = storage.Client(PROJECT_ID)
dst_bucket = storage_client.bucket(BUCKET_NAME1)

#source_blob_name = '1.txt'
destination_file_name = 'C:/Users/jhbae/Downloads/player_info_wirte.csv'

bucket = storage_client.bucket(BUCKET_NAME1)

blob = bucket.blob('player_info_wirte.csv')
blob.upload_from_filename(destination_file_name)
