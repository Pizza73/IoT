#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:08:18 2019

@author: arch
"""

BASE_URL_yahoo='https://map.yahooapis.jp/weather/V1/place'

APP_ID='dj00aiZpPXhoZkFqSkgyRzRBcyZzPWNvbnN1bWVyc2VjcmV0Jng9OTI-'
COORDINATES='135.628998,34.769208' #'135.628998,34.769208'
OUTPUT='json'
url_yahoo=BASE_URL_yahoo+'?appid=%s&coordinates=%s&output=%s' % (APP_ID,COORDINATES,OUTPUT)

#Weather from Weather Hacks 
BASE_URL_wh='http://weather.livedoor.com/forecast/webservice/json/v1'
CITY='270000'
url_wh=BASE_URL_wh+'?city=%s' % (CITY)