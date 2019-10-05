#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:44:29 2019

@author: arch
"""

import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32,GPIO.IN)
    val=GPIO.input(32)
    print(val)
    
    
if __name__=='__main__':
    main()