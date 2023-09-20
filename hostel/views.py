from django.shortcuts import render
from .models import Hostel
import pandas as pd
import googlemaps
import folium
import os

def hotel_map(request):
    hosteldatas = []
    hostel_data = Hostel.objects.all()
    print(hostel_data)
    # print("type", type(map_data))
    for testd in hostel_data:
        print(testd.hostel_name)
        # hosteldatas.append([testd.hostel_id, testd.hostel_score, testd.hostel_name, testd.hostel_addrs, testd.hostel_review, testd.latitude, testd.longitude])

    df = pd.DataFrame(data=hosteldatas, columns=["hostel_id", "hostel_score", "hostel_name", "hostel_addrs", "hostel_review", "latitude", "longitude"])
    # df = pd.DataFrame(data=hosteldatas, columns=["hostel_id", "hostel_score", "hostel_name", "hostel_addrs", "hostel_review"])
    # print(df.columns)
    # print(df.info)
    # gmaps = googlemaps.Client(key='AIzaSyAEcQ0z4mqMLq6RClLRMzxnd6sJSEVVVFY')
    # geocode_result = gmaps.geocode(df.all, language='ko')
    # print(geocode_result)
    # print("host", hosteldatas, len(hosteldatas))

    jeju_latitude = 33.360638  # 제주도 위도
    jeju_longitude = 126.535741  # 제주도 경도

    map_osm = folium.Map(location=[jeju_latitude, jeju_longitude], zoom_start=10)
    # print(map_osm)

    for index, row in df.iterrows():
        hostel_id = row['hostel_id']
        hostel_score = row['hostel_score']
        hostel_name = row['hostel_name']
        hostel_addrs = row['hostel_addrs']
        hostel_review = row['hostel_review']
        latitude = row['latitude']
        longitude = row['longitude']
        if pd.isna(hostel_review):
            continue
        if hostel_score < 8.0:
            marker_color = 'red'
        else:
            marker_color = 'blue'
        popup_text = f'<div style="font-size: 14px; max-width: 400px;">제주도 호텔 {hostel_name}<br>평점: {hostel_score}<br>주소: {hostel_addrs}<br>리뷰: {hostel_review}</div>'
        popup = folium.Popup(popup_text, max_width=400)

        folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon(color=marker_color, icon='info-sign')).add_to(map_osm)

        # print(popup)
        # print(popup_text)
    file_path = "templates/jeju_hotels.html"
    if not os.path.exists(file_path):
        map_osm.save('jeju_hotels.html')    
    templates_name = 'jejumap.html'
    return render(request, templates_name)