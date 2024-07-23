import pygame
from settings import *

class Game():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(resolution)
        print(pygame.display.get_init())
    def run(self):
        self.run = True

        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.flip()
