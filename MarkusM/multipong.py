import pygame as pg
import math
import random as r
import sys

window_width = 400
window_height = 600

pg.init()

window = pg.display.set_mode([window_width,window_height])
run = True





while run:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()



