# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:48:26 2017

@author: AutuanLiu
"""
## 分形图像
import turtle

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    level = 12
    fract(t, -80, 60, 80, 60, level)
    
def fract(t, x1, y1, x2, y2, level):
    # draw bengin at (x1, y1) and end at (x2, y2)
    newX = 0
    newY = 0
    if level == 0:
        drawLine(t, x1, y1, x2, y2)
    else:
        newX = (x1 + x2)/2 + (y2 - y1)/2
        newY = (y1 + y2)/2 - (x2 - x1)/2
        fract(t, x1, y1, newX, newY, level - 1)
        fract(t, newX, newY, x2, y2, level - 1)
            
def drawLine(t, x1, y1, x2, y2):
    # draw line from (x1, y1) to (x2, y2)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

main()