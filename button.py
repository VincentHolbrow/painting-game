import pygame
import settings

class Button():
    def __init__(self, size, position, colour = (0,0,0), text = None, image = None):
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.position = position
        self.hidden = True
        self.prevclick = True
        self.prevrightclick = True
        self.colour = colour

        brightness = (colour[0]+colour[1]+colour[2])/3
        if brightness > 255/2:
            self.detailcol = (0,0,0)
        else:
            self.detailcol = (255,255,255)
        self.image.fill(self.detailcol)
        
        sizeavg = (size[0] + size[1]) /2
        overlaysize = size[0] - sizeavg/10, size[1] - sizeavg/10
        overlay = pygame.Surface(overlaysize)
        overlay.fill(colour)
        if image != None:
            imgrect = image.get_rect()
            imgpos = overlaysize[0]/2 - imgrect.width/2, overlaysize[1]/2 - imgrect.height/2
            overlay.blit(image, (imgpos))

        if text != None:
            font = pygame.font.SysFont('Comic Sans MS', round(size[1]/2))
            overlay.blit(font.render(text, False, self.detailcol), (0,0))

        self.image.blit(overlay, ((size[0] - overlaysize[0])/2, (size[1] - overlaysize[1])/2))

    def clicked(self):
        click = False
        if not self.hidden:
            if not self.prevclick:
                if pygame.mouse.get_pressed()[0]:
                    self.prevclick = True
                    x, y = pygame.mouse.get_pos()
                    if x > self.position[0] and x < self.position[0] + self.rect.width \
                    and y > self.position[1] and y < self.position[1] + self.rect.height:
                        click = True
            else:
                if not pygame.mouse.get_pressed()[0]:
                    self.prevclick = False
        return click

    def rightclicked(self):
        click = False
        if not self.hidden:
            if not self.prevrightclick:
                if pygame.mouse.get_pressed()[2]:
                    self.prevrightclick = True
                    x, y = pygame.mouse.get_pos()
                    if x > self.position[0] and x < self.position[0] + self.rect.width \
                    and y > self.position[1] and y < self.position[1] + self.rect.height:
                        click = True
            else:
                if not pygame.mouse.get_pressed()[2]:
                    self.prevrightclick = False
        return click

    def update(self, screen, text = None):
        if not self.hidden:
            screen.blit(self.image, self.position)
        if not text == None:
            size = self.rect.width, self.rect.height
            self.image.fill(self.detailcol)
            sizeavg = (size[0] + size[1]) /2
            overlaysize = size[0] - sizeavg/10, size[1] - sizeavg/10
            overlay = pygame.Surface(overlaysize)
            overlay.fill(self.colour)

            if text != None:
                font = pygame.font.SysFont('Comic Sans MS', round(size[1]/2))
                overlay.blit(font.render(text, False, self.detailcol), (0,0))

            self.image.blit(overlay, ((size[0] - overlaysize[0])/2, (size[1] - overlaysize[1])/2))

            

    