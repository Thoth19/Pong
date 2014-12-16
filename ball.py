#This file contains the ball class which will hold the data on the ball in pong
import math, os, pygame
from paddle import*
class BallSprite(pygame.sprite.Sprite):
    ''' Is the ball in a game of Pong '''
    GRAVITY = -0.5
    def __init__(self,position, velocity):
        ''' This funcion takes position and velocity as tuples. of the form x,y '''
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(os.path.join("pics","ball.jpg")).convert()
        self.position = position
        self.velocity = velocity
    def update(self,dt):
        # self.position = self.position[0]+self.velocity[0],self.position[1]+self.velocity[1]
        if self.velocity[0] != 0:
            self.rect += self.velocity[0]
            for p in paddles:
                if self.rect.colliderect(p.rect):
                    if self.velocity[0] > 0:
                        self.rect.right = p.rect.left
                        self.velocity = self.velocity[0] *-1 , self.velocity[1]
                    elif self.velocity[0] < 0:
                        self.rect.left = p.rect.right
                        self.velocity = self.velocity[0] *-1 , self.velocity[1]
                    if self.velocity[1] > 0:
                        self.rect.bottom = p.rect.top
                        self.velocity = self.velocity[0], self.velocity[1]*-1
                    elif self.velocity[1] < 0:
                        self.rect.top = p.rect.bottom
                        self.velocity = self.velocity[0], self.velocity[1]*-1

        self.rect.center = self.position