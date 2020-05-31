#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 23:01:50 2019

@author: arch
"""
import requests
import urllib.request
import urllib.parse
import json
import tkinter as tk
import time
from PIL import Image

root=tk.Tk()
root.title('Weather Information')
root.geometry('480x320')

def weather1():
    # Rainfall from yahoo
    BASE_URL_yahoo='https://map.yahooapis.jp/weather/V1/place'

    APP_ID='dj00aiZpPXhoZkFqSkgyRzRBcyZzPWNvbnN1bWVyc2VjcmV0Jng9OTI-'
    COORDINATES='134.295301,33.905606' #'135.628998,34.769208'
    OUTPUT='json'
    url_yahoo=BASE_URL_yahoo+'?appid=%s&coordinates=%s&output=%s' % (APP_ID,COORDINATES,OUTPUT)

    #Weather from Weather Hacks 
    BASE_URL_wh='http://weather.livedoor.com/forecast/webservice/json/v1'
    CITY='270000'
    url_wh=BASE_URL_wh+'?city=%s' % (CITY)

    #get the weather imformation
    html=requests.get(url_yahoo).json()
    data = requests.get(url_wh).json()
    
    #trim the data
    Rain=html['Feature'][0]['Property']['WeatherList']['Weather']
    Rainfall=[]
    
    for i in range(len(Rain)):
        Rainfall.append(Rain[i]['Rainfall'])
        
    Rainfalling=sorted(Rainfall)
    print(Rainfall)
    weather=data['forecasts'][0]['telop']
    print(weather)

    Raining='降雨量：'+str(Rainfall[1])
    print(Raining)
    
    ##Display 
    #root.configure(bg='#FFFFFF')
    Static1 = tk.Label(text=weather, foreground='#000000')
    Static2 = tk.Label(text=Raining, foreground='#000000')
    Static1.pack()
    Static2.pack()
                                          
    #
    for i in Rainfall:
        if i>0:
            print('raining')

    #display image  
    if Rainfall[1]>0:
        image1 = tk.PhotoImage(file = 'caution2.png')
        tk.Label(root, image = image1).pack()
            
    elif '晴' in weather:
        if '曇' in weather:
            print('Partly cloudy')
            image1 = tk.PhotoImage(file = 'partly_cloudy.png')
            tk.Label(root, image = image1).pack()
        elif '雨' in weather:
            print('sandr')
            image1 = tk.PhotoImage(file = 'sandr.png')
            tk.Label(root, image = image1).pack()
        else:
            print('Sunny')
            image1 = tk.PhotoImage(file = 'sunny.png')
            tk.Label(root, image = image1).pack()

    elif '雨' in weather:
        if '曇' in weather:
            print('Partly rainy')
            image1 = tk.PhotoImage(file='partly_rainy.png')
            tk.Label(root, image = image1).pack()
        else:
            print('rainy')
            image1 = tk.PhotoImage(file = 'rainy.png')
            tk.Label(root, image = image1).pack()
        
    else:
        print('cloudy')
        image1 = tk.PhotoImage(file = 'cloudy.png')
        tk.Label(root, image = image1).pack()
    
    root.after(10000,weather1)
    
    import LINE_rainfall
    
weather1()
root.mainloop()