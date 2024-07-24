import pygame
from settings import *
import os

tips = [
    pygame.image.load('Assets/Tips/PenTip.png'),
    pygame.image.load('Assets/Tips/BrushTipVert.png'),
    pygame.image.load('Assets/Tips/BrushTipHor.png'),
    pygame.image.load('Assets/Tips/SmallBrushTip.png')
]

cols = [
    (0,0,0,255),
    (180,0,0,255),
    (0,180,0,255),
    (255,255,255,255),
]

class Canvas():
    def __init__(self, shape):
        self.shape = pygame.image.load('Assets/Shapes/' + shape + '.png')
        self.image = self.shape
        self.rect = self.image.get_rect(center = middlescreen)

        self.edit = False
        self.tip = tips[0]
        self.tipnum = 0
        self.tipcol = cols[0]
        self.colnum = 0

        files = os.listdir('SavedArt')
        self.canvasnum = len(files)

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
        self.tipnum = self.tipnum + change
        if self.tipnum < 0:
            self.tipnum = len(tips) - 1
        elif self.tipnum > len(tips) - 1:
            self.tipnum = 0
        
        self.tip = pygame.mask.from_surface(tips[self.tipnum])
        self.tip = self.tip.to_surface(None, None, None, self.tipcol, (0,0,0,0))

    def cyclecols(self, change):
        self.colnum = self.colnum + change
        if self.colnum < 0:
            self.colnum = len(cols) - 1
        elif self.colnum > len(cols) - 1:
            self.colnum = 0
        self.tipcol = cols[self.colnum]
        self.tip = pygame.mask.from_surface(tips[self.tipnum])
        self.tip = self.tip.to_surface(None, None, None, self.tipcol, (0,0,0,0))

    def saveimg(self):
        pygame.image.save(self.image, ('SavedArt/Canvas') + str(self.canvasnum) + '.png')