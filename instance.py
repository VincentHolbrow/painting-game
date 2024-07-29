import pygame
from settings import *
from canvas import Canvas
import os
from button import Button
from miscdata import *

screens = ['painting', 'pausemenu']

canvases = []

def canvasload():
    files = os.listdir('SavedArt')
    print (files)
    for file in files:
        print (file)
        if not file == '.DS_Store':
            canvases.append(Canvas('Square', file[len(file)-5],\
                                    pygame.image.load('SavedArt/' + file)))
    canvases.append(Canvas('Square', len(files)-1))



class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

        # Initializing buttons
        self.nextbrush = Button((250,50), (0, (resolution[1]/5)), (0,0,0), tipnames[0])
        self.nextcol = Button((250,50), (0, (resolution[1]/5 + 70)), (0,0,0), colnames[0])
        self.quit = Button((300, 75), (middlescreen[0] - 150, middlescreen[1] - 150), (0,0,0), 'Quit')

        self.activescreen = 'painting'
        self.screencol = (0,0,0)

    def buttonupdate(self):
            self.nextbrush.update(self.screen)
            self.nextcol.update(self.screen)
            self.quit.update(self.screen)

    def run(self):
        self.run = True

        canvasload()
        activecan = 0

        while self.run:
            self.clock.tick(FPS)
            self.screen.fill((self.screencol))

            canvas = canvases[activecan]
            for can in canvases:
                if not can == canvas:
                    can.edit = False

            if self.activescreen == 'painting':
                canvas.edit = True
                self.nextbrush.hidden = False
                self.nextcol.hidden = False
                self.quit.hidden = True
                self.screencol = (161,102,47)

            if self.activescreen == 'pausemenu':
                canvas.edit = False
                self.nextbrush.hidden = True
                self.nextcol.hidden = True
                self.quit.hidden = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        canvas.saveimg()
                    if event.key == pygame.K_1:
                        activecan = 0
                    if event.key == pygame.K_2:
                        activecan = 1
                    if event.key == pygame.K_3:
                        activecan = 2
                    if event.key == pygame.K_ESCAPE:
                        if self.activescreen != 'pausemenu':
                            self.prevscreen = self.activescreen
                            self.activescreen = 'pausemenu'
                        else:
                            self.activescreen = self.prevscreen
            if self.nextbrush.clicked():
                canvas.cycletips(1)
                self.nextbrush = Button((250,50), (0, resolution[1]/5), (0,0,0), tipnames[canvas.tipnum])
            if self.nextbrush.rightclicked():
                canvas.cycletips(-1)
                self.nextbrush = Button((250,50), (0, resolution[1]/5), (0,0,0), tipnames[canvas.tipnum])
            if self.nextcol.clicked():
                canvas.cyclecols(1)
                self.nextcol = Button((250,50), (0, resolution[1]/5 + 70), canvas.tipcol, colnames[canvas.colnum])
            if self.nextcol.rightclicked():
                canvas.cyclecols(-1)
                self.nextcol = Button((250,50), (0, resolution[1]/5 + 70), canvas.tipcol, colnames[canvas.colnum])
            if self.quit.clicked():
                self.run = False

            self.buttonupdate()
            canvas.update(self.screen)

            pygame.display.flip()
