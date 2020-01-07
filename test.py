#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:45:52 2020

@author: arch
"""

import requests
from pygame.locals import *
import sys
import time

BASE_URL_yahoo='https://map.yahooapis.jp/weather/V1/place'

APP_ID='dj00aiZpPXhoZkFqSkgyRzRBcyZzPWNvbnN1bWVyc2VjcmV0Jng9OTI-'
COORDINATES='135.628998,34.769208' #'135.628998,34.769208'
OUTPUT='json'
url_yahoo=BASE_URL_yahoo+'?appid=%s&coordinates=%s&output=%s' % (APP_ID,COORDINATES,OUTPUT)

html=requests.get(url_yahoo).json()
print(html)

