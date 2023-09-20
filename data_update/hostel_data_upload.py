import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt_trip.settings")
django.setup()

from hostel.models import Hostel

# review csv
# CSV_PATH = 'hostel/csv/hotel_reviews_delete.csv'

# map csv
CSV_PATH = 'hostel/csv/output.csv'

cnt = 0
with open(CSV_PATH, "r", encoding="UTF-8") as file:
        dataRows = csv.reader(file, skipinitialspace=True)
        dataRows = filter(None, list(dataRows))
        # print(dataRows)
        # map DB INSERT
        for dbData in dataRows:
            # print(dbData[-1])
            # hostel_name = dbData[2]
            # latitude = dbData[5]
            # longitude = dbData[-1]
            if dbData[4] != "" or dbData[5] != "" or dbData[6] != "":
                  hostel_id = dbData[0]
                  hostel_score = dbData[1]
                  hostel_name = dbData[2]
                  hostel_addrs = dbData[3]
                  hostel_review = dbData[4]
                  latitude = dbData[5]
                  longitude = dbData[-1]
                  cnt+=1

                  Hostel.objects.create(
                        hostel_id = hostel_id,
                        hostel_score = hostel_score,
                        hostel_name = hostel_name,
                        hostel_addrs = hostel_addrs,
                        hostel_review = hostel_review,
                        latitude = latitude,
                        longitude = longitude
                    )

              # print(dbData[4])
            # print(cnt)
                  # Hostel.objects.update_or_create(
                  #       hostel_name = hostel_name,
                  #       defaults= {
                  #             "hostel_name" : hostel_name,
                  #             "latitude" : latitude,
                  #             "longitude" : longitude
                  #       }
                  # )
        # review DB INSERT
        # for dbData in dataRows:
        #     hostel_id = dbData[0]
        #     hostel_score = dbData[1]
        #     hostel_name = dbData[2]
        #     hostel_addrs = dbData[3]
        #     hostel_review = dbData[4]
        #     cnt+=1
        # print(cnt)
        
            # Hostel.objects.create(
            #     hostel_id = hostel_id,
            #     hostel_score = hostel_score,
            #     hostel_name = hostel_name,
            #     hostel_addrs = hostel_addrs,
            #     hostel_review = hostel_review
            # )