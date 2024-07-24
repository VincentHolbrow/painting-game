import pygame
from settings import *

class Canvas():
    def __init__(self, shape):
        self.shape = pygame.image.load('Assets/Shapes/' + shape + '.png')
        self.image = self.shape
        self.rect = self.image.get_rect(center = middlescreen)

        self.edit = False

    def update(self, screen):
        if self.edit:
            screen.blit(self.image, (self.rect.left, self.rect.top))
            mousepos = pygame.mouse.get_pos()
            mouseposadjust = (mousepos[0] - self.rect.left, mousepos[1] - self.rect.top)
            tip = pygame.image.load('Assets/Tips/BrushTip.png')

            if pygame.mouse.get_pressed()[0]:
                self.image.blit(tip, mouseposadjust)
            