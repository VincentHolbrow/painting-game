import pygame
from settings import *
from canvas import Canvas
import os

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

    def run(self):
        self.run = True

        canvasload()
        activecan = 0

        while self.run:
            canvas = canvases[activecan]
            for can in canvases:
                can.edit = False
            canvas.edit = True
            self.clock.tick(FPS)
            self.screen.fill((30,30,30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        canvas.cycletips(1)
                    if event.key == pygame.K_LEFT:
                        canvas.cycletips(-1)
                    if event.key == pygame.K_UP:
                        canvas.cyclecols(1)
                    if event.key == pygame.K_DOWN:
                        canvas.cyclecols(-1)
                    if event.key == pygame.K_s:
                        canvas.saveimg()
                    if event.key == pygame.K_1:
                        activecan = 0
                    if event.key == pygame.K_2:
                        activecan = 1
                    if event.key == pygame.K_3:
                        activecan = 2

            canvas.update(self.screen)

            pygame.display.flip()
