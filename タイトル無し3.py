#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:24:00 2019

@author: arch
"""

import pygame
from pygame.locals import *
import sys

#def main():
#   pygame.init()
#   screen = pygame.display.set_mode((480, 320))
#   pygame.display.set_caption("Weather Information")
#   img=pygame.image.load('/home/arch/Documents/Python/caution2.png')
#   
#   font=pygame.font.Font(None,20)
#   word='Hello World'
#   
#   while (1):
#       screen.fill((255,255,255))        # 画面を黒色(#000000)に塗りつぶし
#       screen.blit(img,(0,0))
#       text=font.render(word,True,(0,0,0))
#       screen.blit(text,[400,10])
#       screen.blit(text,[400,30])
#       pygame.display.update()     # 画面を更新
#       # イベント処理
#       for event in pygame.event.get():
#           if event.type == QUIT:  # 閉じるボタンが押されたら終了
#               pygame.quit()       # Pygameの終了(画面閉じられる)
#               sys.exit()
#
#if __name__ == "__main__":
#   main()


print(pygame.font.get_fonts())