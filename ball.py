#This file contains the ball class which will hold the data on the ball in pong
import os, pygame
from paddle import*
from math import *
class BallSprite(pygame.sprite.Sprite):
    ''' Is the ball in a game of Pong '''
    # GRAVITY = -0.5
    def __init__(self,position, velocity):
        ''' This funcion takes position and velocity as tuples. of the form x,y '''
        pygame.sprite.Sprite.__init__(self)
        # self.src_image = pygame.image.load(os.path.join("pics","ball.jpg")).convert()
        self.image = pygame.Surface([16,16])
        self.image.fill((0,0,0))
        # self.image.set_colorkey((0,0,0))
        # pygame.draw.circle(self.image,(255,255,255), position, 8)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velocity = abs(velocity[0]),abs(velocity[1])
        self.vel_dir = copysign(1,velocity[0]),copysign(1,velocity[1])
    def update(self):
        # self.image=pygame.transform.rotate(self.src_image,0)
        self.rect.x += self.velocity[0] * self.vel_dir[0]
        self.rect.y += self.velocity[1] * self.vel_dir[1]


