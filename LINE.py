#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:00:16 2020

@author: arch
"""

curl -v -X POST https://api.line.me/v2/bot/message/broadcast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {uuDcgrnY6jVi46SNbWFz2nCQMvNqEwyim/8z2DXMxAYOMv02M+kDG/o/pUUX2ufo1JqXIaDpa8F/DgK5FDVHSvuYqhcHAEYDxlNebW+LUp56rHUpN5YpH8HH9RqjGR7wq5Pc51PxZvwxKZbW61/BJAdB04t89/1O/w1cDnyilFU=}' \
-d '{
    "messages":[
        {
            "type":"text",
            "text":"熱中症を発症するリスクが低くなったので、窓を開けてエアコンを消しました"
        },
        {
            "type":"text",
            "text":"部屋の状態\n温度：25℃\n湿度：50％"
        }
    ]
}'