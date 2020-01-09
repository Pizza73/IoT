#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:28:35 2020

@author: arch
"""

import serial
import time

#ser=serial.Serial('/dev/serial/by-path/pci-0000:00:14.0-usb-0:3:1.0-port0',9600)

ser=serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0',9600,bytesize=serial.SEVENBITS)


while True:
    data='128'
    ser.write(bytes(data,'UTF-8'))
    print('forward')
    time.sleep(2)
    print('stop')
    data='192'
    ser.write(bytes(data,'UTF-8'))
    time.sleep(2)
    data='255'
    ser.write(bytes(data,'UTF-8'))
    print('backward')
    time.sleep(2)
    data='0'
    ser.write(bytes(data,'UTF-8'))
    ser.close()
    break

#ser = serial.Serial()
#ser.port = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"     #デバイスマネージャでArduinoのポート確認
#ser.baudrate = 9600 #Arduinoと合わせる
#ser.setDTR(False)     #DTRを常にLOWにしReset阻止
#ser.bytesize=serial.SEVENBITS
#ser.open()            #COMポートを開く
#ser.write(b'1')       #送りたい内容をバイト列で送信
    
    
#ser.close()
    
    

