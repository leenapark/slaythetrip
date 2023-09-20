import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt_trip.settings")
django.setup()

from weather_trip.models import WeatherData

CSV_PATH = 'weather_trip\datas\weather_data.csv'

with open(CSV_PATH, "r", encoding="UTF-8") as file:
        dataRows = csv.reader(file, skipinitialspace=True)
        dataRows = filter(None, list(dataRows))
        for dbData in dataRows:
            wdate = dbData[0].strip()
            temp_avg = dbData[1].strip()
            temp_sense = dbData[2].strip()
            w_txt = dbData[3].strip()
            w_state = dbData[4].strip()
            rain_mm = dbData[5].strip()
            hum_avg = dbData[6].strip()
            ws_dir = dbData[7].strip()
            ws_avg = dbData[8].strip()
            sun_txt = dbData[9].strip()
            sun_time = dbData[10].strip()
            dust_avg = dbData[11].strip()
            dust_state = dbData[12].strip()
            micro_dust_avg = dbData[13].strip()
            micro_dust_state = dbData[14].strip()
            ozone_avg = dbData[15].strip()
            ozone_state = dbData[16].strip()
            air_score = dbData[17].strip()
            air_state = dbData[18].strip()
            # print(dbData[18].strip())


        WeatherData.objects.create(
            wdate = wdate,
            temp_avg = temp_avg,
            temp_sense = temp_sense,
            w_txt = w_txt,
            w_state = w_state,
            rain_mm = rain_mm,
            hum_avg = hum_avg,
            ws_dir = ws_dir,
            ws_avg = ws_avg,
            sun_txt = sun_txt,
            sun_time = sun_time,
            dust_avg = dust_avg,
            dust_state = dust_state,
            micro_dust_avg = micro_dust_avg,
            micro_dust_state = micro_dust_state,
            ozone_avg = ozone_avg,
            ozone_state = ozone_state,
            air_score = air_score,
            air_state = air_state
        )