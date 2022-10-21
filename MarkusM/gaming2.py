import pygame as pg
import random as r
import sys, time
import os

pg.init() #starter pygame

window_width = 1080
window_height = 720
window = pg.display.set_mode([window_width,window_height],pg.RESIZABLE)
pg.display.set_caption('gaming')
font = pg.font.SysFont("Arial", 24)
gifList = []

for i in range(43):
    gifList.append(pg.image.load(f"ELV_IT2_UW/MarkusM/gif_test/breaking-bad-money-{i}.png"))
    

print(type(window))

#fps
clock = pg.time.Clock() 
currentFps = 0
averageFps = 0
frames_counter = 0

def fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, True, (0,0,0))
	return fps_text



while True: #displayLoop

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

            
    #frames_counter +=1
    #if frames_counter == 61 or frames_counter >= 61:
    #    frames_counter =0
    #if frames_counter <= 60 and frames_counter >=30:
    #    window.fill((135,206,235))
    #else:
    #    window.fill((0,0,0))
    #print(frames_counter)
    window.fill((255,255,255))
    
    frames_counter +=1

    if frames_counter == 45:
        frames_counter =0
    


        
    window.blit(font.render(str(frames_counter),True,(0,0,0)),(400,20))
    #if now > 0 and not now < 30:
    #    window.fill((0,0,0))
    #else:

    window.blit(fps(),(20,20))
    



    clock.tick(60)
    pg.display.flip()

    
