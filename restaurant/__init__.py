import os

if os.environ.get('RUN_MAIN', None) != 'true':
    print("ml 모델 load")
    default_app_config = 'load.LoadConfig'
