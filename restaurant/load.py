### load.py

from django.apps import AppConfig
import pickle

# add : global load model
class LoadConfig(AppConfig):
   with open('restaurant\models\model.pkl', 'rb') as f:
        tfidf_vect = pickle.load(f)
        lr_clf = pickle.load(f)
        
        def ready(self):
            pass