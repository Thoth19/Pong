import math, os, pygame
paddles = []
class PaddleSprite(pygame.sprite.Sprite):
    '''
    This is the user controlled paddle in a game of Pong
    '''
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        paddles.append(self)
        self.rect=pygame.Rect(position[0], position [1], 16, 128)
    def move(self, position):
        ''' moves to given position'''
        self.rect=pygame.Rect(position[0], position [1], 16, 128)
