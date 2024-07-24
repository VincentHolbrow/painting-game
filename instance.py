import pygame
from settings import *
from canvas import Canvas

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

    def run(self):
        self.run = True

        #reformat
        canvas = Canvas('Square')
        canvas.edit = True

        while self.run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    print('yup')
                    if event.key == pygame.K_RIGHT:
                        canvas.cycletips(1)
                    if event.key == pygame.K_LEFT:
                        canvas.cycletips(-1)

            canvas.update(self.screen)

            pygame.display.flip()
