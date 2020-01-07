#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:26:32 2020

@author: arch
"""

import serial
import time

ser=serial.Serial('/dev/ttyUSB0',19200)

for i in range(10):
    ser.write('64')
    time.sleep(0.5)
    
ser.close()
