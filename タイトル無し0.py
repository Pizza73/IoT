#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:48:16 2018

@author: arch
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt



def main():
    cap=cv2.VideoCapture(0)
    def nothing(x):
        pass
    
    cv2.namedWindow('bar')
    h_L=cv2.createTrackbar('H_L','bar',0,255,nothing) #0 
    s_L=cv2.createTrackbar('S_L','bar',0,255,nothing) #0
    v_L=cv2.createTrackbar('V_L','bar',145,255,nothing) #240
    h_H=cv2.createTrackbar('H_H','bar',255,255,nothing) #255
    s_H=cv2.createTrackbar('S_H','bar',255,255,nothing) #255
    v_H=cv2.createTrackbar('V_H','bar',255,255,nothing) #255
    
    while True:
        ret,frame=cap.read()
        image2=np.asarray(frame)
        gray=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
        hsv=cv2.cvtColor(image2,cv2.COLOR_BGR2HSV)
        
        h_L = cv2.getTrackbarPos('H_L','bar')
        s_L = cv2.getTrackbarPos('S_L','bar')
        v_L = cv2.getTrackbarPos('V_L','bar')
        h_H = cv2.getTrackbarPos('H_H','bar')
        s_H = cv2.getTrackbarPos('S_H','bar')
        v_H = cv2.getTrackbarPos('V_H','bar')
        
        
        lower=(h_L,s_L,v_L)
        upper=(h_H,s_H,v_H)
        
        
        mask=cv2.inRange(hsv,lower,upper)
        
        cv2.imshow('hsv',mask)
        
        