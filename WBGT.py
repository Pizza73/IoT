#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 08:25:59 2020

@author: arch
"""

def WBGT(temp,humi):
    if temp <=5:
        wet_temperature=5-(6.7-6.7*humi/100)
        
    elif temp <= 10:
        wet_temperature=10-(8.4-8.4*humi/100)
        
    elif temp <= 15:
        wet_temperature=15-(10.2-10.2*humi/100)
        
    elif temp <= 20:
        wet_temperature=20-(12.2-12.2*humi/100)
        
    elif temp <= 25:
        wet_temperature=25-(14.4-14.4*humi/100)
        
    elif temp <= 30:
        wet_temperature=30-(16.6-16.6*humi/100)
        
    elif temp <= 35:
        wet_temperature=35-(18.9-18.9*humi/100)
        
    elif temp <= 40:
        wet_temperature=40-(21.2-21.2*humi/100)
        
    else:
        wet_temperature=45-(23.6-23.6*humi/100)
        
    WBGT=0.7*wet_temperature+0.3*temp
    
    return WBGT