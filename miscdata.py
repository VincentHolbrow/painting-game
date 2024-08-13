import pygame
from settings import *
tipnames = ['Pen', 'Brush Vertical', 'Brush Horizontal', 'Small Brush']
colnames = ['Black', 'Cadmium Red', 'Deep Rose','Soft Pumpkin','Electric Orange', 'Soleil', 'Banana Yellow', 
            'Forest Green', 'Mint', 'Navy', 'Baby Blue', 'Lavender', 'Gentle Violet', 'White']
pygame.font.init()
mainfont = pygame.font.SysFont('Comic Sans MS', round(resolution[1]/40))