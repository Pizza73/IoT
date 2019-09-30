#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:54:10 2019

@author: arch
"""
import requests
import urllib.request
import urllib.parse
import json
import pygame
from pygame.locals import *
import sys
from . import ID

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 320))
    pygame.display.set_caption("Weather Information")
    
    # Rainfall from yahoo
    BASE_URL_yahoo='https://map.yahooapis.jp/weather/V1/place'

    APP_ID=ID.APP_ID
    COORDINATES='135.628998,34.769208' #'135.628998,34.769208'
    OUTPUT='json'
    url_yahoo=BASE_URL_yahoo+'?appid=%s&coordinates=%s&output=%s' % (APP_ID,COORDINATES,OUTPUT)

    #Weather from Weather Hacks 
    BASE_URL_wh='http://weather.livedoor.com/forecast/webservice/json/v1'
    CITY='270000'
    url_wh=BASE_URL_wh+'?city=%s' % (CITY)
    
    font=pygame.font.Font(None,20)
    
    while (1):
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
    
        Raining='Rainfall: '+str(Rainfall[1])+' mm/h'
        print(Raining)        
        
        for i in Rainfall:
            if i>0:
                print('raining')

        #display image  
#        if Rainfall[1]>0:
#            img = pygame.image.load('/home/arch/Documents/Python/caution2.png') 
            
        if '晴' in weather:
            if '曇' in weather:
                weather='partly cloudy'
                print('Partly cloudy')
                if Rainfall[1]>0:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/caution2.png') 
                else:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/partly_cloudy.png') #partly_cloudy.png
            elif '雨' in weather:
                weather='sunny and rainy'
                print('sandr')
                if Rainfall[1]>0:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/caution2.png') 
                else:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/sandr.png') 
            else:
                weather='sunny'
                print('Sunny')
                if Rainfall[1]>0:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/caution2.png') 
                else:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/sunny.png')

        elif '雨' in weather:
            if '曇' in weather:
                weather='cloudy and rainy'
                print('Partly rainy')
                if Rainfall[1]>0:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/caution2.png') 
                else:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/partly_rainy.png')
            else:
                weather='rainy'
                print('rainy')
                if Rainfall[1]>0:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/caution2.png') 
                else:
                    img = pygame.image.load('/home/arch/Documents/Python/Weather/rainy.png') 
        
        else:
            weather='cloudy'
            print('cloudy')
            if Rainfall[1]>0:
                img = pygame.image.load('/home/arch/Documents/Python/Weather/caution2.png') 
            else:
                img = pygame.image.load('/home/arch/Documents/Python/Weather/cloudy.png') 
        
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
        
        screen.fill((255,255,255))
        screen.blit(img,(0,0))  #座標指定
        text1=font.render(weather,True,(0,0,0)) #色指定
        text2=font.render(Raining,True,(0,0,0))
        screen.blit(text1,[350,10])
        screen.blit(text2,[350,30])
        pygame.display.update()
        pygame.time.wait(60000)                                    
            
if __name__=="__main__":
    main()

