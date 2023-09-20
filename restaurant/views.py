from django.shortcuts import render
from restaurant.models import Hotplace, Sample
# from restaurant.ml_model import mlExcute
import pandas as pd
import re
# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

# add : global load model
from . import load
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

from konlpy.tag import Okt
from manage import ok_tokenizer

@csrf_exempt
@api_view(['POST', 'GET'])
def restaurant(request):

    hotplaces = Hotplace.objects.all()
    # samples = Sample.objects.all()
    # print(request.POST.get("name"))
    
    # for testq in list_q:
    #     print(type(testq))


    datas = []
    df1 = Sample.objects.all()
    for test in df1:
        datas.append([test.placeName, test.review_detail, test.satisfaction_rate])
    df1 = pd.DataFrame(data=datas, columns=["placeName", "review_detail", "satisfaction_rate"])

    def remove_emoji(inputString):
        emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                  "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', inputString) # no emoji
    

     # df1 데이터 전처리
    df1['review_detail'] = df1['review_detail'].apply(lambda x : re.sub(r'(?:\b[0-9a-zA-Zㄱ-ㅎㅏ-ㅣ]\b|[?!\W]+)\s*', ' ', x).strip())
    df1['review_detail'] = df1['review_detail'].apply(lambda x : re.sub('[ㄱ-ㅎㅏ-ㅣ]+', ' ', x))

    df1['review_detail'] = df1['review_detail'].apply(remove_emoji)
    
  
    con = {
            "h_place": hotplaces
            }
    return render(
        request,
        'restaurant/restaurant.html', con
    )

def ajax(request):
    word_d = [""]
    if request.method == "POST":
            word_d=[]
            # print(request.POST.get("selectedPlace"))
            selectedPlace = request.POST.get("selectedPlace")
        # selectedPlace = request.POST['selectedPlace']
            # print(selectedPlace)
            word_d.append(selectedPlace)
        # print("word", word_d)
    word = str(word_d[0])
    # print(word)
    queryData = Sample.objects.filter(placeName__startswith=word).values("placeName", "review_detail")

    list_q = queryData.all()
    list_q = list(list_q)
    
    json_data = json.dumps(list_q, cls=DjangoJSONEncoder, ensure_ascii=False)
    print(json_data)
    return HttpResponse(json_data, content_type ="application/json")

@csrf_exempt
def selapi(request):
  if request.method == "POST":
    try:
      option = json.loads(request.body)
      option = option.get("data")  # 선택한 값 가져오기
      # option 값에 따른 처리 수행
      print("test", option)
    except json.JSONDecodeError as e:
        print("error")



    ok_tokenizer(option)
 
    tfidf_vect = load.LoadConfig.tfidf_vect
    lr_clf = load.LoadConfig.lr_clf
    print("tfidf_vect", tfidf_vect)
    print("lr_clf", lr_clf)
    data = pd.Series(option)
    tfidf_data = tfidf_vect.transform(data)
    print("tfidf_data")

    if lr_clf.predict(tfidf_data)[0] == 1:
        print("긍정")
        result = ["긍정"]
        print("type", type(result), result)
        json_post = json.dumps(result, cls=DjangoJSONEncoder, ensure_ascii=False)

        print(json_post)

        return HttpResponse(json_post, content_type ="application/json")
    else:
        print("부정")
        result = ["부정"]
        print("type", type(result), result)
        json_post = json.dumps(result, cls=DjangoJSONEncoder, ensure_ascii=False)

        print(json_post)

        return HttpResponse(json_post, content_type ="application/json")


  else:
    return render(
        request,
        'restaurant/restaurant.html'
    )
