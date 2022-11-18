import pygame as pg, random as rnd
_, clock, wind, counter, score, Vballs, balls, box = pg.init(), pg.time.Clock(), pg.display.set_mode([500, 500]), 0, 0, [[2.5, 3.2]], [pg.Rect(250, 200, 10, 10)], pg.Rect(200, 450, 100, 15)
while True:  
    for event in pg.event.get(): 
        if event.type == pg.QUIT: pg.quit()
    if pg.key.get_pressed()[pg.K_LEFT]: box.move_ip(-10, 0)
    if pg.key.get_pressed()[pg.K_RIGHT]: box.move_ip(10, 0)          
    for x in range(len(balls)): 
        Vballs[x][1] = -Vballs[x][1] if box.collidepoint(balls[x].x, balls[x].y + 10) else Vballs[x][1]
        score = score + 1 if box.collidepoint(balls[x].x, balls[x].y + 10) else score
        if balls[x].y + 10 >= wind.get_height(): pg.quit()
    
        
         
        Vballs[x][0] = -Vballs[x][0] if ((balls[x].x - 10) <= 0 or (balls[x].x + 10) >= wind.get_width()) else Vballs[x][0]
        Vballs[x][1] = -Vballs[x][1] if ((balls[x].y - 10) <= 0 or (balls[x].y + 10) >= wind.get_height()) else Vballs[x][1]         
        balls[x].move_ip(Vballs[x][0], Vballs[x][1]), pg.draw.circle(wind, (255, 0, 0), (balls[x].x, balls[x].y), 10)
    counter, _ = counter + 1, (wind.blit(pg.font.SysFont("Arial", 16).render(str(score), True, 0), (470, 20)), pg.draw.rect(wind, 0, box), pg.display.flip(), clock.tick(60), wind.fill((255, 255, 255)))  
    if counter % 360 == 0: balls.append(pg.Rect(rnd.randint(10, 490), rnd.randint(10, 250), 10, 10)), Vballs.append([rnd.choice([1, -1]) * 2.5, 3.2])