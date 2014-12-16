from ball import*
from paddle import*
import math,os,pygame

pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

ball_group=pygame.sprite.Group()
paddle_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

p1 = PaddleSprite((32,32))
paddle_group.add(p1)
all_sprites_group.add(p1)
p2 = PaddleSprite((32,534))
paddle_group.add(p2)
all_sprites_group.add(p2)
ball = BallSprite((32,128),(0,1))
ball_group.add(ball)
all_sprites_group.add(ball)

while True:
    clock.tick(60)
    screen.fill((255,0,0))
    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT]:
    #     p1.move(p1.rect.left - 2, p1.rect.top, 16,128)
    # if key[pygame.K_RIGHT]:
    #     p1.move(p1.rect.left + 2, p1.rect.top, 16,128)
    #     print "pushed right"
    for event in pygame.event.get():
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print mouse_pos
            p1.rect.x = mouse_pos[0]
            print p1.rect.x
    # for p in paddle_group:
    #     pygame.draw.rect(screen, (255,255,0), p.rect)
    # ball_group.update()
    all_sprites_group.draw(screen)
    # print "hep"
    pygame.display.flip()