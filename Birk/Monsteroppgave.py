from pylab import *
import sys, time, random

def slow_type(t):
    typing_speed = 100 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

"""class Monster:
    def __init__(self, navn, lv, str, hp, chr):
        self.navn = navn
        self.lv = lv
        self.str = str
        self.hp = hp
        self.chr = chr
        
"""
