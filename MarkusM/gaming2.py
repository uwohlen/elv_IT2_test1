import pygame as pg
import random as r
import sys, time
import os
from pygame.locals import *

pg.init() #starter pygame

window_width = 1080
window_height = 720
window = pg.display.set_mode([window_width,window_height],pg.RESIZABLE)
pg.display.set_caption('gaming')
font = pg.font.SysFont("Arial", 24)
gifList = []
keyIndex = 0

#acceptedKeys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class key:
    def __init__(self,key,pressed):
        self.key = key
        self.pressed = pressed
    def keyPress(self,id):
        print("")
        

k_a = key(1,False)
k_b = key(2,False)
k_c = key(3,False)
k_d = key(4,False)
k_e = key(5,False)
k_f = key(6,False)
k_g = key(7,False)
k_h = key(8,False)
k_i = key(9,False)
k_j = key(10,False)
k_k = key(11,False)
k_l = key(12,False)
k_m = key(13,False)
k_n = key(14,False)
k_o = key(15,False)
k_p = key(16,False)
k_q = key(18,False)
k_r = key(18,False)
k_s = key(19,False)
k_t = key(20,False)
k_u = key(21,False)
k_v = key(22,False)
k_w = key(23,False)
k_x = key(24,False)
k_y = key(25,False)
k_z = key(26,False)
k_æ = key(27,False)
k_ø = key(28,False)
k_å = key(29,False)
KeyList = [k_a,k_b,k_c,k_d,k_e,k_f,k_g,k_h,k_i,k_j,k_k,k_l,k_m,k_n,k_o,k_p,k_q,k_r,k_s,k_t,k_u,k_v,k_w,k_x,k_y,k_z,k_æ,k_ø,k_å]



for i in range(44):
    gifList.append(pg.image.load(f"MarkusM/gif_test/breaking-bad-money-{i}.png"))


print(type(window))

#fps
clock = pg.time.Clock() 
currentFps = 0
averageFps = 0
frames_counter = 0
typetest = []
keypressed = False

def fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, True, (0,0,0))
	return fps_text



while True: #displayLoop

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        if event.type == pg.KEYDOWN:
            print("")
            #finne hvilken som er trykket

        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                #finne hvilken som er trykket
                keypressed = False

            
    #frames_counter +=1
    #if frames_counter == 61 or frames_counter >= 61:
    #    frames_counter =0
    #if frames_counter <= 60 and frames_counter >=30:
    #    window.fill((135,206,235))
    #else:
    #    window.fill((0,0,0))
    #print(frames_counter)

    if frames_counter == 44:
        frames_counter =0

    window.fill((255,255,255))
    window.blit(gifList[frames_counter],(0,0))
    
    frames_counter +=1

    


        
    window.blit(font.render(str(frames_counter),True,(0,0,0)),(400,20))
    #if now > 0 and not now < 30:
    #    window.fill((0,0,0))
    #else:

    window.blit(fps(),(20,20))

    keyPress = pg.key.get_pressed()


    if keyPress[K_w] and keypressed == False:
        typetest.append(("W"))
        keypressed = True
    if keyPress[K_RETURN]:
        typetest.clear()


    for i in range(len(typetest)):
        window.blit(font.render(str(typetest[i]),True,(0,0,0)),(20*i,200))
        


    clock.tick(24)
    pg.display.flip()

    
