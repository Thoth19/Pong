from ball import*
from paddle import*
from wall import*
import math,os,pygame
#Set up screen
pygame.init()
screen = pygame.display.set_mode([800,640])
clock = pygame.time.Clock()

ball_group=pygame.sprite.Group()
paddle_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
#Create actors
p1 = PaddleSprite((32,32))
paddle_group.add(p1)
all_sprites_group.add(p1)
p2 = PaddleSprite((350,640-16-32))
paddle_group.add(p2)
all_sprites_group.add(p2)
ball = BallSprite((400,320),(1,3))
ball_group.add(ball)
all_sprites_group.add(ball)
for i in range(50):
    for j in range(40):
        if j == 0 or j == 39 or i == 0 or i == 49:
            wall = WallSprite((i*16,j*16))
            wall_group.add(wall)
            all_sprites_group.add(wall)
    #creates walls around the game board, only on edges
done = False
score = 0 
while not(done):
    clock.tick(60) #limits FPS
    screen.fill((255,0,0)) #resets screen. should only refresh changed bits

    for event in pygame.event.get():
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            p1.move(mouse_pos)
            # Paddle 1 follows mouse
    lowest_ball = ball
    for ball in ball_group:
        #ball will handle the collisions
        if ball.velocity[0] != 0: #if ball doesn't move in x, don't need to check
            old_x = ball.rect.x
            ball.rect.x += ball.velocity[0]*ball.vel_dir[0]
            for p in paddle_group: #check collisions
                if ball.rect.colliderect(p.rect):
                    if ball.vel_dir[0] > 0:
                        if ball.rect.x < p.rect.x+43:
                            ball.x_dir() #bounce back if in first third
                        elif p.rect.x+43<=ball.rect.x<=p.rect.x+85:
                            ball.velocity = 0, ball.velocity[1] #bounce straight if in middle
                        else:
                            # bounce forward in last
                            pass
                        # in the third case we dont change velocity
                    ball.rect.x = old_x # don't go through the paddle
            hit_x = False
            for w in wall_group:
                if ball.rect.colliderect(w.rect):
                    ball.x_dir()
                    hit_x = True #matters for win/loss conditions
                    break
        if ball.velocity[1] != 0:
            ball.rect.y += ball.velocity[1] * ball.vel_dir[1]
            for p in paddle_group:
                if ball.rect.colliderect(p.rect):
                    if ball.vel_dir[1] > 0:
                        ball.rect.bottom = p.rect.top
                        ball.y_dir()
                    elif ball.vel_dir[1] < 0:
                        ball.rect.top = p.rect.bottom
                        ball.y_dir()
                    # always bounce in y when hit a paddle
                    if ball.velocity[0] == 0:
                        if ball.rect.x < p.rect.x+43:
                            ball.x_dir()
                            ball.velocity = ball.velocity[0] + 1, ball.velocity[1]
                        elif p.rect.x+43<=ball.rect.x<=p.rect.x+85:
                            pass
                        else:
                            ball.velocity = ball.velocity[0] + 1, ball.velocity[1]
            # for w in wall_group:
            #     if ball.rect.colliderect(w.rect) and not(hit_x):
            #     # if a side wall is hit, then we don't want to bounce down.
            #     # since this code can never run, it doesn't matter, but stays in 
            #         ball.y_dir()
            #         break
            #     else:
            #         pass
            ball.velocity = ball.velocity[0], ball.velocity[1] + 1
            # speed increases over time
        if ball.rect.y > lowest_ball.rect.y:
            # for Paddle two to chase it. In case there is eventually another ball
            lowest_ball = ball

    if ball.rect.y < 32:
        pygame.display.quit()
        print "You lose a point"
        score -= 1
        ball.reset((400,320),(1,3))
    #add tkinter interface and then allow to reset the game?
    elif ball.rect.y > 640-16-32:
        pygame.display.quit()
        print "You win a point"
        score += 1
        ball.reset((400,320),(1,3))
    if score >5:
        print " You win the match"
        break
    elif score <-5:
        print "You lose the match"
        break
        
    if p2.rect.x + p2.rect.width< lowest_ball.rect.x + lowest_ball.rect.width /2:
        p2.move((p2.rect.x + min(5,abs(lowest_ball.rect.x-p2.rect.x)),p2.rect.y))
    elif p2.rect.x > lowest_ball.rect.x:
        p2.move((p2.rect.x - min(5,abs(lowest_ball.rect.x-p2.rect.x)),p2.rect.y))
    #paddle 2 follows the lowest ball

    all_sprites_group.update()
    all_sprites_group.draw(screen)
    pygame.display.flip()


