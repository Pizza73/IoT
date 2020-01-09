#!/bin/sh

curl -v -X POST https://api.line.me/v2/bot/message/broadcast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {uuDcgrnY6jVi46SNbWFz2nCQMvNqEwyim/8z2DXMxAYOMv02M+kDG/o/pUUX2ufo1JqXIaDpa8F/DgK5FDVHSvuYqhcHAEYDxlNebW+LUp56rHUpN5YpH8HH9RqjGR7wq5Pc51PxZvwxKZbW61/BJAdB04t89/1O/w1cDnyilFU=}' \
-d '{
    "messages":[
        {
            "type":"text",
            "text":"熱中症を発症するリスクが高くなったので、窓を閉めてエアコンをつけました"
        },
        {
            "type":"text",
            "text":"部屋の状態\n温度：30℃\n湿度：80％"
        }
    ]
}'