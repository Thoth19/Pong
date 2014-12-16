import math, os, pygame
class PaddleSprite(pygame.sprite.Sprite):
    '''
    This is the user controlled paddle in a game of Pong
    '''
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([128,16])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
    def move(self, position):
        ''' moves to given position'''
        self.rect=pygame.Rect(position[0], position [1], 16, 128)
