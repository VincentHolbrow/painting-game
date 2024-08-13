import pygame
from settings import *

tips = [
    pygame.image.load('Assets/Tips/PenTip.png'),
    pygame.image.load('Assets/Tips/BrushTipVert.png'),
    pygame.image.load('Assets/Tips/BrushTipHor.png'),
    pygame.image.load('Assets/Tips/SmallBrushTip.png')
]

outlines = [
    pygame.image.load('Assets/Tips/PenTipOutline.png'),
    pygame.image.load('Assets/Tips/BrushTipVertOutline.png'),
    pygame.image.load('Assets/Tips/BrushTipHorOutline.png'),
    pygame.image.load('Assets/Tips/SmallBrushTipOutline.png')
]

cols = [
    (0,0,0,255),
    (227,0,34,255),
    (199,71,103,255),
    (225,161,109),
    (255,93,53),
    (252,233,189),
    (255,225,53),
    (63,90,54,255),
    (62,180,137,255),
    (0,0,128),
    (137,207,240),
    (220,208,255),
    (78,64,105),
    (255,255,255)
]

class Canvas():
    def __init__(self, shape, num, image = None):
        self.shape = pygame.image.load('Assets/Shapes/' + shape + '.png')
        self.image = self.shape
        if not image == None:
            self.image.blit(image, (0,0))
        self.rect = self.image.get_rect(center = middlescreen)

        self.edit = False
        self.tip = tips[0]
        self.tipnum = 0
        self.tipcol = cols[0]
        self.colnum = 0
        self.canvasnum = num
        self.outline = outlines[self.tipnum]

    def update(self, screen):
        if self.edit:
            screen.blit(self.image, (self.rect.left, self.rect.top))

            screen.blit(self.outline, pygame.mouse.get_pos(), None, pygame.BLEND_RGB_SUB)

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
        self.outline = outlines[self.tipnum]

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