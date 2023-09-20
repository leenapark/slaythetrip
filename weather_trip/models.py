from django.db import models

# Create your models here.
class WeatherData(models.Model):
    wdate = models.CharField(max_length=30, verbose_name='날짜(측정일자)')
    temp_avg = models.CharField(max_length=30, verbose_name='평균기온')
    temp_sense = models.CharField(max_length=30, verbose_name='체감온도')
    w_txt = models.CharField(max_length=30, verbose_name='전날 날씨와 비교')
    w_state = models.CharField(max_length=30, verbose_name='날씨상태')
    rain_mm = models.CharField(max_length=30, verbose_name='강수량(mm)')
    hum_avg = models.CharField(max_length=30, verbose_name='평균습도')
    ws_dir = models.CharField(max_length=30, verbose_name='풍향')
    ws_avg = models.CharField(max_length=30, verbose_name='평균풍속')
    sun_txt = models.CharField(max_length=30, verbose_name='일출,일몰')
    sun_time = models.CharField(max_length=30, verbose_name='일출,일몰 시간')
    dust_avg = models.IntegerField(default=0, verbose_name='평균 미세먼지 농도')
    dust_state = models.CharField(max_length=30, verbose_name='미세먼지 상태')
    micro_dust_avg = models.IntegerField(default=0, verbose_name='평균 초미세먼지 농도')
    micro_dust_state = models.CharField(max_length=30, verbose_name='초미세먼지 상태')
    ozone_avg = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='평균 오존량')
    ozone_state = models.CharField(max_length=30, verbose_name='오존상태')
    air_score = models.IntegerField(default=0, verbose_name='대기질 수치')
    air_state = models.CharField(max_length=30, verbose_name='대기질 상태')
    
    class Meta:
        verbose_name_plural = "날씨 데이터"

