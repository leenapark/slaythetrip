from django.views import View
from django.shortcuts import render

from .models import WeatherData

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse

import csv
import django
import sys
import os

sys.path.append("C:\playdata_lab\slaythetrip\weather_trip\package")

import weather_nuri_v3 as wn
import json

def weather_trip(request):

    wtest = wn.temperatures()

    weather_datas = WeatherData.objects.all()

    for data in weather_datas:
        weather_data = data

    context = {
        'weather_data' : weather_data,
        "temp_l_h" : wtest
    }
    return render(request, "weather_trip/weather.html", context)


@api_view(['POST', 'GET'])
# 날씨 예측모델
@api_view(['POST', 'GET'])
def ajax(request):
    if request.method == "POST":
        check = request.POST.get("borough")

    # print("check", check)
    
    # 이건 나중에 구현
    # model = keras.models.load_model('/models/weather_pre_model.h5')
    # pred_temp = model.predict(check)
    # 날짜, 예측결과(평균온도)
    pred_temp = 20.4
    context = {
        
        'req_date' :check,  'pred_temp': pred_temp 
    }

    return render(request, "weather_trip/weather.html", context)