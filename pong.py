from ball import*
from paddle import*
import math,os,pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
p1 = PaddleSprite((32,32))
p2 = PaddleSprite((32,568))
ball = BallSprite((32,128),(0,1))
ball_group=pygame.sprite.RenderPlain(ball)
while True:
    dt=clock.tick(60)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        p1.move(p1.rect.left - 2, p1.rect.right, 16,128)
    if key[pygame.K_LEFT]:
        p1.move(p1.rect.left + 2, p1.rect.right, 16,128)
    for p in paddles:
        pygame.draw.rect(screen, (255,255,0), p.rect)
    screen.fill((0,0,0))
    ball_group.update(dt)
    ball_group.draw(screen)
    pygame.display.flip()