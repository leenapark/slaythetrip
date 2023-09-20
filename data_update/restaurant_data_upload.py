import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt_trip.settings")
django.setup()

from restaurant.models import hotplace, Sample

CSV_PATH1 = 'restaurant/datas/db_data/restaurant_2023-06-21.csv'
CSV_PATH2 =  "restaurant/datas/ml_data/sample_data.csv"

with open(CSV_PATH1, "r", encoding="UTF-8") as file:
    data_rows = csv.reader(file, skipinitialspace=True)
    # header(첫번째 줄) 제외
    next(data_rows, None) 

    
    # 공백라인을 제거하기 위해서
    data_rows = list(data_rows)
    # print("전 ", data_rows)
    data_rows = list(filter(None, data_rows))
    # print("후 ", data_rows)

    # DB 테이블에 한 레코드씩 입력하기
    for row in data_rows:
    # print(row[0])
      if row[0] != None or row[0] != '':
        hotplace.objects.create(
        place_name = row[0],
        place_address = row[1],
        review_num = row[2],
        score_rate = row[3],
        phone_num = row[4],
        )

with open(CSV_PATH2, "r", encoding="UTF-8") as file:
    data_rows = csv.reader(file, skipinitialspace=True)
    next(data_rows, None)

    for row in data_rows:
        # print(ck)
        placeName = row[0]
        satisfaction_rate = row[1]
        review_detail = row[2]


        Sample.objects.create(
            placeName = placeName,
            satisfaction_rate = satisfaction_rate,
            review_detail = review_detail
        )