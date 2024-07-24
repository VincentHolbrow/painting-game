import pygame
from settings import *

tips = [
    pygame.image.load('Assets/Tips/PenTip.png'),
    pygame.image.load('Assets/Tips/BrushTipVert.png'),
    pygame.image.load('Assets/Tips/BrushTipHor.png'),
    pygame.image.load('Assets/Tips/SmallBrushTip.png')
]

class Canvas():
    def __init__(self, shape):
        self.shape = pygame.image.load('Assets/Shapes/' + shape + '.png')
        self.image = self.shape
        self.rect = self.image.get_rect(center = middlescreen)

        self.edit = False
        self.tip = tips[0]

    def update(self, screen):
        if self.edit:
            screen.blit(self.image, (self.rect.left, self.rect.top))

            mousepos = pygame.mouse.get_pos()
            mposadj = (mousepos[0] - self.rect.left, mousepos[1] - self.rect.top)
            move = pygame.mouse.get_rel()
            magnitude = round((move[0]**2 + move[1]**2)**0.5)

            if pygame.mouse.get_pressed()[0]:
                for i in range(magnitude):
                    pos = round(mposadj[0] - i*(move[0]/magnitude)), \
                        round(mposadj[1] - i*(move[1]/magnitude))
                    self.image.blit(self.tip, pos)
    
    def cycletips(self, change):
        tipnum = tips.index(self.tip) + change
        if tipnum < 0:
            tipnum = len(tips) - 1
        elif tipnum > len(tips) - 1:
            tipnum = 0
        print(tipnum)
        self.tip = tips[tipnum]