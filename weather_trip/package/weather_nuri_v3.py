import requests as req
from bs4 import BeautifulSoup as bs
import datetime
import os
import csv

def temperatures():


    url = "https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=184"
    res = req.get(url)
    soup = bs(res.content, 'html.parser')

    # 테이블 head 추출
    w_head = soup.select(".tab-menu-cont div.over-scroll:nth-of-type(5) thead tr th")
    day_list = []
    for head in w_head:
        # print(head)
        if "colspan" in head.attrs :
            # print("여기를 pass 함")
            continue
        text = list(head.strings)
        # print("text", text)
        day_list.append(text)
    # print("days", day_list)

    # 날씨 데이터 수집 처리
    w_infos = soup.select(".tab-menu-cont div.over-scroll:nth-of-type(5) tbody tr")
    cities_weather = {}
    for w_info in w_infos:
        city_weather = {}
        for idx, city_w in enumerate(w_info.select("td")): 
            # print(city_w)
            if "rowspan" in city_w.attrs :
                if "7" in city_w.attrs["rowspan"]:
                    # print("여기를 pass 함")
                    continue
            # 도시 추출
            span = city_w.select_one("span")
            if "class" in span.attrs:
                if "sticky" in span.attrs["class"]:
                    city = span.get_text(strip=True)

                else:
                    # 도시의 온도 추출
                    # print(city_w)
                    temp = list(city_w.strings)
                    del temp[1]  # / 삭제
                    # print(temp)
                    # print(idx)
                    if idx == 2 :
                        city_weather[day_list[idx-2][0]] = temp
                        # print("ck", city_weather[day_list[idx-2][0]])
                    else:
                        city_weather[day_list[idx-3][0]] = temp
                    # print(city_weather)
        # print(city_weather)

        # 지역별 날씨
        cities_weather[city] = city_weather

    return cities_weather

